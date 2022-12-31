from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url="account_login")
def dashboard(request):
    return render(request,"account/dashboard/dashboard.html")