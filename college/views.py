from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from . import models

from event import urls

# from django.http import HttpResponse
# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect
    return render(request,'authentication/signup.html')

def about_view(request):
    return render(request,'mainlink/aboutus.html')
def contact_view(request):
    return render(request,'mainlink/contact.html')

def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect
    
    return render(request,'mainlink/adminclick.html',{'event': 'calendar' })
def staffclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect
    return render(request,'mainlink/staffclick.html')
def studentclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect
    return render(request,'mainlink/studentclick.html')

def student_signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect
    return render(request,'authentication/signup.html')

def student_signin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect
    return render(request,'authentication/signin.html')

def index_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect
    return render(request,'mainlink/index.html')



