from django.db import models

class UserInfoModel(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField(max_length=15, blank=False)
    dateofbirth=models.DateField(max_length=25)
    password=models.CharField(max_length=15) 
class LoginModel(models.Model):
    name=models.CharField(max_length=25)
    password=models.CharField(max_length=15)
class ContentModel(models.Model):
    title=models.CharField(max_length=25)
    image=models.ImageField()
    content=models.CharField(max_length=250)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)