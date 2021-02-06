from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'base.html')

def login(request):
    return render(request, 'login.html')

def test(request):
    return render(request, 'test.html')