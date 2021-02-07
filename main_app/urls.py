from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('home/', views.home, name='home'),
    path('food/<int:id>/', views.food, name='food_form'),
    path('food/<int:id>/delete', views.food_delete, name='food_delete'),
    path('poop/<int:id>/', views.poop, name='poop_form'),
    path('poop/<int:id>/delete', views.poop_delete, name='poop_delete'),
    path('test/', views.test, name='test'),
    path('accounts/signup/', views.signup, name='signup')
]