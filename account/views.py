from account.models import Profile
from django.contrib.auth import forms
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.

#signup
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"],
                password=request.POST["password1"],)
            nickname = request.POST["nickname"]
            address = ["address"]
            profile = Profile(user=user, nickname=nickname, address=address)
            profile.save()
            auth.login(request,user)
            return redirect('main')
        else:
            return render (request, 'signup.html')
    else:
        form = UserCreationForm()
        return render (request, 'signup.html')
#login
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'login.html', {'form':form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})

#logout
def logout(request):
    auth.logout(request)
    return redirect('main')