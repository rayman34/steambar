var pos = -100;
var box = document.getElementById("box");
var gear1 = document.getElementById("gear1");
var gear2 = document.getElementById("gear2");
var gear3 = document.getElementById("gear3");
var gear4 = document.getElementById("gear4");
var gear5 = document.getElementById("gear5");
var gear6 = document.getElementById("gear6");
var gear7 = document.getElementById("gear7");
var gear8 = document.getElementById("gear8");
var gear9 = document.getElementById("gear9");
var gear10 = document.getElementById("gear10");
var v = pos>=100;
var crement = pos+=1;
var place = "right";
var t = setInterval(move, 1,t);

function move1(info){
	if (place == "right"){
		place = "left";
		pos = -100;
	}else{
		pos = 0;
		place = "right"
	}
}
function move(t){
	if (place == "left"){
		v = pos>=0;
		crement = pos+=1;
	}else{
		v = pos<=-100;
		crement = pos-=1;
	}
	if(v){
		clearInterval(t);
		return;
	}
	else{
		crement;
		box.style.left = pos+"%";
		gear1.style.rotate = -pos*3+"deg";
		gear2.style.rotate = pos*3+"deg";
		gear3.style.rotate = -pos*3+"deg";
		gear4.style.rotate = pos*3+"deg";
		gear5.style.rotate = -pos*3+"deg";
		gear6.style.rotate = pos*3+"deg";
		gear7.style.rotate = -pos*3+"deg";
		gear8.style.rotate = pos*3+"deg";
		gear9.style.rotate = -pos*3+"deg";
		gear10.style.rotate = pos*3+"deg";
	}
}
