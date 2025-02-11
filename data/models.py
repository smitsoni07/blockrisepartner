from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.core.validators import MinLengthValidator

class MyModel(models.Model):
	fullname = models.CharField(max_length=50)
	username = models.CharField(max_length=50)
	email = models.EmailField(max_length=50, unique=True,default=False)
	password = models.CharField(max_length=128)
	created_at = models.DateTimeField(default=timezone.now)
	updated_at = models.DateTimeField(auto_now=True)
	balance = models.IntegerField(default=0,blank=True, null=True)
	requiset = models.IntegerField(default=0,blank=True, null=True)
	condition = models.CharField(max_length=50,blank=True)

class data(models.Model):
	fullname = models.CharField(max_length=50)
	email = models.EmailField(max_length=50, unique=True,default=False)
	phone_number = models.CharField(max_length=20, validators=[MinLengthValidator(10)])
	subject = models.CharField(max_length=50)
	message = models.CharField(max_length=350)