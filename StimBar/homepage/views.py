from django.shortcuts import render
import sqlite3
import os
import requests
import json

def index(request):
    return render(request,'homepage/homepage.html', {"message": "Welcome to Python"})

def get_prod(request):
    return render(request,'homepage/homepage.html', {"object_list": {"name":"some","price":"3000","some":"3000"}})

def get_html(url,params=None):
    r = requests.get(url,params=params)
    return r

def clean_json(s):
    s = json.loads(s)
    s_list = str(s['basket']).replace("[\"{'","")
    s_list = s_list.replace("}\"]",",")
    s_list = s_list.replace("'","")
    s_list = s_list.replace(":"," X ")
    bas_list = []
    one_pos = ""
    bas_list_num = []
    one_num = ""
    for i in range(len(s_list)):
        if s_list[i] == ",":
            bas_list.append(one_pos)
            one_pos = ""
        else:
            one_pos = one_pos+s_list[i]
    bas_list.append("\nНомер телефона: "+s['number'][0])
    return bas_list

def get_form(request):
    if request.method == 'POST':
        print(request)
        file = open("request","a")
        string = str(request.POST)
        string = string.replace("<","")
        string = string.replace(">","")
        string = string.replace("QueryDict: ","")
        string = string.replace("\"","_|_")
        string = string.replace("'","\"")
        string = string.replace("_|_","'")
        string = clean_json(string)
        file.write("\n"+str(string))
        file.close()
        text = ""
        for i in range(len(string)):
            text = text+"\n"+str(string[i].replace("_"," "))
        url = "https://api.telegram.org/bot1540961936:AAHwcnrBsgVE0DE-dCd9e-KTNT2gxztCvek/sendMessage?chat_id=104932971&text="+str(text)
        get_html(url)
    return render(request,'homepage/sender.html', {"object_list": {"name":"some","price":"3000","some":"3000"}})

def state_read(request):
    conn = sqlite3.connect('db.sqlite3')
    file = open("homepage/templates/homepage/includes/test.html",'r')
    data = file.read()
    file.close()
    print(data)
    cat0 = {"Соусы":data}
    cursor = conn.cursor()
    cats = ["Холодные закуски","Горячие закуски","Салаты","Стейки","Гарниры","Напитки","Супы","Колбаски","Соусы","Бургеры","Техасское барбекю"]
    for z in range(len(cats)):
        cursor.execute("SELECT name FROM homepage_positions WHERE parent = '"+str(cats[z])+"'")
        names = cursor.fetchall()
        cursor.execute("SELECT price FROM homepage_positions WHERE parent = '"+str(cats[z])+"'")
        prices = cursor.fetchall()
        cursor.execute("SELECT image FROM homepage_positions WHERE parent = '"+str(cats[z])+"'")
        src = cursor.fetchall()
        data = '\n'
        for i in range(len(names)):
            name = names[i][0].replace(" ","_")    
            data = data+'\n'+'<style type="text/css">.photo_'+name+'\n'+'{background: url('+src[i][0]+'); background-size: 100%;}\n.id_'+name+'{width:15%; font-size: 33px; height:50%;color:white;background:black;left:31%;top:25%;display:inline-block;text-align:center;position:relative;}'+'</style>'+'\n'+'<div class="food_inside">'+'\n'+'     <div class="food_gear">'+'\n'+'          <div class="photo_pos photo_'+name+'"></div>'+'\n'+'     </div>'+'\n'+'     <div class="info_block">'+'\n'+'         <div class="name_pos">'+'\n'+'             <h3>'+names[i][0]+'</h3>'+'\n'+'         </div>'+'\n'+'         <div class="price">'+'\n'+'             <h3 id="id_price_'+name+'">'+prices[i][0]+'</h3>'+'\n'+'         </div>'+'\n'+'         <div class="but_box">'+'\n'+'             <input class="g_button g_plus" name="someName" type="button" value="+" onclick="change_num(\''+name+'\',\'+\')">'+'\n'+'             <div class="id_'+name+'">'+'\n'+'                 <div class="alert">0</div>'+'\n'+'             </div>'+'\n'+'             <input class="g_button g_minus" name="someName" type="button" value="-" onclick="change_num(\''+name+'\',\'-\')">'+'\n'+'         </div>'+'\n'+'     </div>'+'\n'+'</div>'

        file = open('homepage/templates/homepage/includes/'+str(cats[z])+'.html','w')
        file.write(data)
        file.close()
    
    conn.close()
    return render(request,'homepage/homepage.html', cat0)

def change_base(request):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM homepage_positions")
    results = cursor.fetchall()
    for i in range(len(results)):
        cursor.execute("SELECT image FROM homepage_positions WHERE id = '"+str(results[i][0])+"'")
        image = cursor.fetchall()[0][0]
        insert = image.replace("homepage/static/homepage/positions/","static/homepage/positions/")
        cursor.execute("UPDATE homepage_positions SET image = '"+str(insert)+"' WHERE id = '"+str(results[i][0])+"'")
    conn.commit()
    conn.close()
    return render(request,'homepage/homepage.html', {"message": "Welcome to Python"})
    