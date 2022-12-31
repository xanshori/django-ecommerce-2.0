from django.shortcuts import render
from django.contrib.auth.hashers import check_password
# Create your views here.

def home(request):
    return render(request,"home/home.html")