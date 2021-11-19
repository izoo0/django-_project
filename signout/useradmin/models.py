from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SignOut(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     from_date = models.DateField()
     to_date = models.DateField()
     loction = models.CharField(max_length = 20)
     reason = models.TextField(max_length=50)
     status = models.TextField(default=0)

     def __str__(self):
          return self.loction
