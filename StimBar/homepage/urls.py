from django.conf.urls import url,include
from . import views
from django.views.generic import ListView, DetailView
from homepage.models import Positions

soup = ListView.as_view(queryset=Positions.objects.filter(parent='Супы'),template_name="homepage/homepage.html")
food_list = {'objects':soup}



urlpatterns = [
    url(r'^$', views.state_read, name='state_read'),
   # url(r'^$',ListView.as_view(queryset=Positions.objects.all().order_by("-id"),template_name="homepage/homepage.html")),
   # url(r'^$',soup),
    url(r'^form/$', views.get_form, name='get_form'),
    url(r'^photo/$', views.change_base, name='change_base')
]