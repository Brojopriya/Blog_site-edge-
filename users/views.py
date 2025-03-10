from django.shortcuts import render
from django.contrib.auth.models import User

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if username is None or email is None or password is None:
            return render(request,"400.html",status=400)
        
        emails_exists= User.objects.filter(email=email).exists()
        if emails_exists:
            return render(request,"400.html",status=400)
        if password != confirm_password:
            return render(request,"400.html",status=400)
        
        User.objects.create_user(email=email,username=username,password=password)
        return render(request,"register.html")
        
    
    else:    
        return render(request,"register.html")

# Create your views here.
