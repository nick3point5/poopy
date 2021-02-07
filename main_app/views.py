from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import  PoopForm



# Create your views here.
def start(request):
    return render(request, 'base.html')

def home(request):
    poop_list= Poop.objects.all()
    food_list = Food.objects.all()
    context={
        'poop_list':poop_list,
        'food_list':food_list
    }
    return render(request, 'content/home.html', context)

def food_add(request):

    return render(request, 'content/food_form.html')

def poop_add(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = PoopForm()
        else:
            poop = Poop.objects.get(pk=id)
            form = PoopForm(instance=poop)
        context = {
            'form': form
        }
        return render(request, "content/poop_form.html", context)
    else:
        if id == 0:
            form = PoopForm(request.POST)
        else:
            Poop = Poop.objects.get(pk=id)
            form = PoopForm(request.POST,instance= Poop)
        if form.is_valid():
            new_poop = form.save(commit=False)
            new_poop.user_id = request.user.id
            new_poop.save()
        return redirect('home')


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