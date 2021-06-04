from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from apps.models import Profile
from .forms import ProfileForm


def user_profile(request):
    profiles = Profile.objects.all()
    return render(request, 'registration/user_profile.html', {'profiles': profiles})

def edit_profile(request):
    profile = Profile.objects.all()
    
    if request.method == 'POST':
        form = ProfileForm(data=request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm() 
    
    return render (request, 'registration/edit_profile.html', {'form': form})


def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('apps:home')
    
    context = {'form': form}
    return render(request, 'registration/register.html', context)


