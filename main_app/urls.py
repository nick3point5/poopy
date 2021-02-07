from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('home/', views.home, name='home'),
    path('food/add', views.food_add, name='food_form'),
    path('poop/add', views.poop_add, name='poop_form'),
    path('test/', views.test, name='test'),
    path('accounts/signup/', views.signup, name='signup')
]