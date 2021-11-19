from django.shortcuts import render,redirect
from .forms import AddSignOut
from django.contrib import messages
from django.views.generic import ListView
from .models import SignOut

# Create your views here.

def student_dash(request):
          form = AddSignOut(request.POST or None)
          if form.is_valid():
               form.save()
               messages.success(request,('post is a success'))
               return redirect('dashboard')
          return render(request,"dashboard.html",{'form':form})

class Signout(ListView):
     model = SignOut
     template_name = "signout.html"
          




