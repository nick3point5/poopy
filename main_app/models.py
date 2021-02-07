from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    url = models.CharField(max_length=200, null=True)

class Color(models.Model):
    color = models.CharField(max_length=50)
    def __str__(self):
        return self.color

class Bristol_Type(models.Model):
    type = models.CharField(max_length=50)
    def __str__(self):
        return self.type
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
class Poop(models.Model):
    pass_date = models.DateField(auto_now=True, auto_now_add=False)
    note = models.TextField(max_length=250, null=True)
    type = models.ForeignKey(Bristol_Type)
    color = models.ForeignKey(Color)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Food(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ate_date = models.DateField(auto_now=True, auto_now_add=False)
    note = models.TextField(max_length=250, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
