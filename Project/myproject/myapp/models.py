from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    Profile_pic = models.ImageField(upload_to='media/')



# Signup Model:
class Signup_model(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField()
    confirm_password = models.CharField()
    
