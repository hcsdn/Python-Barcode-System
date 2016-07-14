"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
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
class RegisterForm(forms.Form):
   username=forms.CharField(max_length=254,
                            widget=forms.TextInput({
                                'class':'form-control',
                                'placeholder':'User Name'}))
   password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
   confirmedpassword = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Confirmed Password'}))
   email = forms.CharField(label=_("Password"),
                               widget=forms.EmailInput({
                                   'class': 'form-control',
                                   'placeholder':'Email'}))
   
   firstname=forms.CharField(max_length=254,
                            widget=forms.TextInput({
                                'class':'form-control',
                                'placeholder':'First Name'}))
   lastname=forms.CharField(max_length=254,
                            widget=forms.TextInput({
                                'class':'form-control',
                                'placeholder':'Last Name'}))
 