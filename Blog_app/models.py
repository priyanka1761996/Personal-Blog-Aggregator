from django.forms import ModelForm
from django import forms
from django.db import models
from django.contrib.auth.models import User


class LoginForm(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    

class Blogger(models.Model):
    blogger_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    followers = models.ManyToManyField(User, related_name='following', blank=True)
    

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/",max_length=500)
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE)
   

        
    