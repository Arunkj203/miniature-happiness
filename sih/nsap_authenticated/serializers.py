from rest_framework import serializers
from .models import User

class loginSerializer(serializers.Serializer):
    
       	username = serializers.CharField(max_length=100, read_only=True)
	    password = serializers.CharField(max_length=100, min_length=8, style={'input_type': 'password'})
	    token = serializers.CharField(max_length=255, read_only=True)