from .models import SignOut
from django.forms import ModelForm

class AddSignOut(ModelForm):
     class Meta:
          model = SignOut
          fields = ('user','from_date','to_date','loction','reason')