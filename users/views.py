from django.shortcuts import render, redirect
from users.forms import UserRegistrationFrom
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
        context = {"form": form}
        return render(request,"register.html",context)
        
    if request.method == "GET": 
        context = { "form": UserRegistrationFrom()}
        return render(request,"register.html",context)
    

def login_view(request): 
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("post-list")
        
        context = {"form": form}
        return render(request,"login.html",context)
        
    if request.method == "GET": 
        context =   { "form": AuthenticationForm()}
        return render(request,"login.html",context)
    
def logout_view(request):
    logout(request)
    return redirect("login")

 

# Create your views here.
