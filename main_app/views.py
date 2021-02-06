from django.shortcuts import render, redirect

# Create your views here.
def login(request):
    return render(request, 'login.html')

def test(request):
    return render(request, 'test.html')