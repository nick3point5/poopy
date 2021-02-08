from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
import uuid
import boto3
from .models import Poop, Food, Photo
from .forms import  PoopForm, FoodForm
from django.contrib.auth.decorators import login_required

S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'poopytoilet'

# Create your views here.
def start(request):
    return render(request, 'base.html')

@login_required
def home(request):
    poop_list= Poop.objects.all().order_by('-pass_date')
    food_list = Food.objects.all().order_by('-ate_date')
    context={
        'poop_list':poop_list,
        'food_list':food_list
    }
        
    return render(request, 'content/home.html', context)

@login_required
def food_delete(request,id):
    food = Food.objects.get(pk=id)
    food.delete()
    return redirect('/home')

@login_required
def food(request, id=0):
    photo = None
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
            photo_file = request.FILES.get('photo-file', None)
            if photo_file:
                s3 = boto3.client('s3')
                key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
                try:
                    s3.upload_fileobj(photo_file, BUCKET, key)
                    url = f"{S3_BASE_URL}{BUCKET}/{key}"
                    photo = Photo(url=url)
                except:
                    print('An error occurred uploading file to S3')

            form = FoodForm(request.POST)
        else:
            photo_file = request.FILES.get('photo-file', None)
            if photo_file:
                s3 = boto3.client('s3')
                key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
                try:
                    s3.upload_fileobj(photo_file, BUCKET, key)
                    url = f"{S3_BASE_URL}{BUCKET}/{key}"
                    photo = Photo(url=url)
                except:
                    print('An error occurred uploading file to S3')
            this_food = Food.objects.get(pk=id)
            form = FoodForm(request.POST,instance= this_food)

    if form.is_valid():
        new_food = form.save(commit=False)
        if photo:
            photo.save()
            new_food.image_id = photo.id
        new_food.user_id = request.user.id
        new_food.save()
    return redirect('home')

@login_required
def poop(request, id=0):
    photo = None
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
            photo_file = request.FILES.get('photo-file', None)
            if photo_file:
                s3 = boto3.client('s3')
                key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
                try:
                    s3.upload_fileobj(photo_file, BUCKET, key)
                    url = f"{S3_BASE_URL}{BUCKET}/{key}"
                    photo = Photo(url=url)
                except:
                    print('An error occurred uploading file to S3')

            form = PoopForm(request.POST)
        else:
            photo_file = request.FILES.get('photo-file', None)
            if photo_file:
                s3 = boto3.client('s3')
                key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
                try:
                    s3.upload_fileobj(photo_file, BUCKET, key)
                    url = f"{S3_BASE_URL}{BUCKET}/{key}"
                    photo = Photo(url=url)
                except:
                    print('An error occurred uploading file to S3')
            this_poop = Poop.objects.get(pk=id)
            form = PoopForm(request.POST,instance= this_poop)

    if form.is_valid():
        new_poop = form.save(commit=False)
        if photo:
            photo.save()
            new_poop.image_id = photo.id
        new_poop.user_id = request.user.id
        new_poop.save()
    return redirect('home')

@login_required
def poop_delete(request,id):
    poop = Poop.objects.get(pk=id)
    poop.delete()
    return redirect('/home')


def login(request):
    return render(request, 'registration/login.html', )

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