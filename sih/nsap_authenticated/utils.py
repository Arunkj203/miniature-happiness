
from django.conf import settings
from datetime import datetime, timedelta
import jwt


def generate_access_token(user):
	payload = { "Message":"Sucess Succes"}

	access_token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
	return access_token