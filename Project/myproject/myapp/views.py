from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm


# SignupForm view:

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        return render(request, "myapp/signup.html", {"form":form})
    else:
            form = SignupForm()
            return render(request, "myapp/signup.html", {"form":form})

#L login_view

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("profile")
        return render(request, "myapp/login.html", {'error': "Invalid username  or password"})
    else:
        return render(request, "myapp/login.html")


def profile_view(request):
    return render(request, "myapp/profile.html")

def logout_view(request):
    logout(request)
    return redirect("signup")