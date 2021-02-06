from django.db import models

# Create your models here.
class Image(models.Model):
    url = models.CharField(max_length=200)

class Color(models.Model):
    color = models.CharField(max_length=50)
    def __str__(self):
        return self.color

class Poop(models.Model):
    pass_date = models.DateField(auto_now=True, auto_now_add=False)
    Bristol_Type = models.IntegerField()
    note = models.CharField(max_length=250)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

class Food(models.Model):
    ate_date = models.DateField(auto_now=True, auto_now_add=False)
    note = models.CharField(max_length=250)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    poop_id = models.ForeignKey(Poop, on_delete=models.CASCADE)
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE)
