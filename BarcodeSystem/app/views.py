"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.forms import RegisterForm

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })

def register(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    form = RegisterForm(request.POST or None)
    return render(request,
        'app/register.html',       
        {
            'form':form,
            'title':'Register',
            'message':'Register a new account.',
            'year':datetime.now().year,
        })

def saveUser(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    form = RegisterForm(request.POST or None)

    return render(request,
        'app/register.html',       
        {
            'form':form,
            'title':'Register',
            'message':'Register a new account.',
            'year':datetime.now().year,
        })
