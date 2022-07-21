from django.shortcuts import render
from django.http import HttpResponse
from .models import gc
from json import dumps



# Create your views here.

y=[]

def home(request):
    return render(request,"home.html")

def dec(request):
    if request.method=="POST":
      return render(request,"clc.html",{"k":True})
    else:
     return render(request,"clc.html",{"k":False,"m":True})
def gpc(request):
    return render(request,"gc.html",{"m":False})
  
def mark(request):
   sem=request.POST['sem']
   dept=request.POST['dept']
   #Entry.objects.values_list('id', 'headline')
   ls=gc.objects.filter(dept=dept).values_list(sem)
   

   x=ls[0][0].split(":")
   sb=[]
   for i in x:
    if(i.isnumeric()):
        y.append(i)
    else:
        sb.append(i)

   return render(request,"gc.html",{"m":True,"ls":sb})

def cal(request):
    ls=[["O",10],["A+",9],["A",8],["B+",7],["B",6],["RA",0]]
    data = dumps(ls)
    
    cp = dumps(y)


    return render(request,"temp.html",{'dat':data,"cp":cp})

def cg(request):

    
        sem=request.POST['sem']
        gp=[]
        sm=int(sem)
        for i in range(sm):
             gp.append(i+1)
        return render(request,"clc.html",{"m":False,"sm":gp})

   
