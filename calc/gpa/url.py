from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("gpc",views.gpc,name="gpc"),
    path("mark",views.mark,name="mark"),
    path("cal",views.cal,name="cal"),
    path("dec",views.dec,name="dec"),
    path("cg",views.cg,name="cg")

]
