from django.contrib import admin
from .models import Image, Color, Poop, Food, Bristol_Type

# Register your models here.
admin.site.register(Image)
admin.site.register(Color)
admin.site.register(Poop)
admin.site.register(Food)
admin.site.register(Bristol_Type)
