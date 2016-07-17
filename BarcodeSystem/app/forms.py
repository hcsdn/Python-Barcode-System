"""
Definition of forms.
"""

from django import forms
#from app.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

#class RegisterForm(UserCreationForm):
#   username = forms.CharField(max_length=254,
#                            widget=forms.TextInput({
#                                'class':'form-control',
#                                'placeholder':'User Name'}))
#   password1 = forms.CharField(label=_("Password"),
#                               widget=forms.PasswordInput({
#                                   'class': 'form-control',
#                                   'placeholder':'Password'}))
#   password2 = forms.CharField(label=_("Password"),
#                               widget=forms.PasswordInput({
#                                   'class': 'form-control',
#                                   'placeholder':'Confirmed Password'}))
#   email = forms.CharField(label=_("Password"),
#                               widget=forms.EmailInput({
#                                   'class': 'form-control',
#                                   'placeholder':'Email'}))
   
#   first_name = forms.CharField(max_length=254,
#                            widget=forms.TextInput({
#                                'class':'form-control',
#                                'placeholder':'First Name'}))
#   last_name = forms.CharField(max_length=254,
#                            widget=forms.TextInput({
#                                'class':'form-control',
#                                'placeholder':'Last Name'}))
#   class Meta:
#       model = User
#       fields = ("username",)

#   def saveUser(self):
#        user = super(RegisterForm, self).save()
#        user.save()
#        return user
   
        
 