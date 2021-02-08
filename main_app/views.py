from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
import uuid
import boto3
from .models import *
from .forms import  PoopForm, FoodForm


S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'poopytoilet'



# Create your views here.
def start(request):
    return render(request, 'base.html')

def home(request):
    poop_list= Poop.objects.all().order_by('-pass_date')
    food_list = Food.objects.all().order_by('-ate_date')
    context={
        'poop_list':poop_list,
        'food_list':food_list
    }
    for poop in poop_list:
        dt = poop.image.url
        print()
        
    return render(request, 'content/home.html', context)

def food(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = FoodForm()
        else:
            this_food = Food.objects.get(pk=id)
            form = FoodForm(instance=this_food)
        context = {
            'form': form
        }
        return render(request, "content/food_form.html", context)
    else:
        if id == 0:
            form = FoodForm(request.POST)
        else:
            this_food = Food.objects.get(pk=id)
            form = FoodForm(request.POST,instance= this_food)
        if form.is_valid():
            new_food = form.save(commit=False)
            new_food.user_id = request.user.id
            new_food.save()
        return redirect('home')

def food_delete(request,id):
    food = Food.objects.get(pk=id)
    food.delete()
    return redirect('/home')

def poop(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = PoopForm()
        else:
            this_poop = Poop.objects.get(pk=id)
            form = PoopForm(instance=this_poop)
        context = {
            'form': form
        }
        return render(request, "content/poop_form.html", context)
    else:
        if id == 0:
            form = PoopForm(request.POST)
        else:
            this_poop = Poop.objects.get(pk=id)
            form = PoopForm(request.POST,instance= this_poop)
        if form.is_valid():
            new_poop = form.save(commit=False)
            new_poop.user_id = request.user.id
            new_poop.save()
        return redirect('home')

def poop_delete(request,id):
    poop = Poop.objects.get(pk=id)
    poop.delete()
    return redirect('/home')

def login(request):
    return render(request, 'registration/login.html', )

def test(request):
    return render(request, 'test.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            # login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    # A GET or a bad POST request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)