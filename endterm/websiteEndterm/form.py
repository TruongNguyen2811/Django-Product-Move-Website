from django.forms import ModelForm
from websiteEndterm.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm (UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
class Factoryform (ModelForm):
    class Meta:
        model = factory
        fields = '__all__'
class Storeform (ModelForm):
    class Meta:
        model = store
        fields = '__all__'
class WarrantyCenterform (ModelForm):
    class Meta:
        model = warrantycenter
        fields = '__all__'
class Adminform (ModelForm):
    class Meta:
        model = admin
        fields = '__all__'