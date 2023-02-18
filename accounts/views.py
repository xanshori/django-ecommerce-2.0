from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile,Ip
from .forms import ProfileForm
# Create your views here.

@login_required(login_url="account_login")
def dashboard(request):
    return render(request,"account/dashboard/dashboard.html")




def profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method =="POST":
        ipaddr=request.META['REMOTE_ADDR']
        try:
            ipuser = Ip.objects.get(profile=profile)
            if ipuser.ip != ipaddr:
                Ip.objects.create(
                    profile=profile,
                    ip=ipaddr
                ).save()
        except:
            Ip.objects.create(
                profile=profile,
                ip=ipaddr
            ).save()
        profileform = ProfileForm(request.POST or None,instance=profile)
        if profileform.is_valid():
            profileform.save()
            profile.save()
            
            return redirect('accounts:profile')
    else:
        profileform = ProfileForm(instance=profile)
    context={
        'title':'edit | profile',
        'profileforms':profileform,
        'profile':profile,
    }
    return render(request,'account/dashboard/edit_profile.html',context)


