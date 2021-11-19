from django.urls import path
from . import views 
from .views import user_login,user_register

urlpatterns = [
   path('',views.user_login,name="user-login"),
   path('registration-page',views.user_register,name="user-register")  
]