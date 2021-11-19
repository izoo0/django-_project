from django.urls import path
from . import views 
from .views import student_dash,Signout

urlpatterns = [
   path('',views.student_dash,name="dashboard"), 
   path('signout_summary',Signout.as_view(), name = "sigouts")
]