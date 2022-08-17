from django.contrib import admin
from django.urls import re_path,include,path
from .views  import login,show


urlpatterns = [
   path(r'',login.as_view()),
   path(r'show/',show.as_view()),
]