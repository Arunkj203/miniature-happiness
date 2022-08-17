from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User,auth
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import AuthenticationFailed
from django.shortcuts import render,get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import generate_access_token
import jwt
import csv
import pandas as pd
from wsgiref.util import FileWrapper
from django.template.response import TemplateResponse
import json 



class login(APIView):     
     authentication_classes = (TokenAuthentication,)
     permission_classes = (AllowAny,)

     def get(self,request):
          
          return render(request,"login.html")
     def post(self,request):
          
               usernm=request.POST['unm']
               password=request.POST['pass']

               df = pd.read_csv("D:\dataset\census_data.csv")
               json_records = df.reset_index().to_json(orient ='records')
               arr = []
               arr = json.loads(json_records)
               ct= {'d': arr}
    

               if not usernm:
                   raise AuthenticationFailed('A user name is needed.')

               if not password:
                   raise AuthenticationFailed('An password is needed.')
               us=authenticate(username=usernm,password=password)

               if us and us.is_active:
                 user_access_token = generate_access_token(us)
                 response = Response()
                 response.set_cookie(key='access_token', value=user_access_token, httponly=True)
                 response.data = {
                 'access_token': user_access_token
				 }			    
                 auth.login(request,us)
                 #return Response("login succes")
                
                 return  render(request,"table.html",ct) 

               else:
                 return  render(request,"login.html",{"m":True}) 

class show(APIView):
      authentication_classes = (TokenAuthentication,)
      permission_classes = (AllowAny,)
      def get(self, request):
        return render(request,"table.html")
        user_token = request.COOKIES.get('access_token')

        if not user_token:
           raise AuthenticationFailed('Unauthenticated user.')
        
        payload = jwt.decode(user_token, settings.SECRET_KEY, algorithms=['HS256'])
        msg=payload["Message"]
        #return response(msg)
        return render(request,"sih.html")
     

        