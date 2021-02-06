from django.db import models

# Create your models here.
class Image(models.Model):
    url = models.CharField(max_length=200, null=True)

class Color(models.Model):
    color = models.CharField(max_length=50)
    def __str__(self):
        return self.color

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

class Poop(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pass_date = models.DateField(auto_now=True, auto_now_add=False)
    Bristol_Type = models.IntegerField(default=3)
    note = models.CharField(max_length=250, null=True)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)

class Food(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ate_date = models.DateField(auto_now=True, auto_now_add=False)
    note = models.CharField(max_length=250, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)