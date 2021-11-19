from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def user_login(request):
     if request.method == "POST":
          username = request.POST['username']
          password = request.POST['password']
          user = authenticate(request,username=username,password=password)
          if user is not None:
               login(request,user)
               return redirect('dashboard')
          else:
               messages.success(request,('error login in'))
               return redirect('user-login')
     else:
          return render(request, "home.html",{})

def user_register(request):
     return render(request,"user-reg.html",{})
