from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
def render_index(request):
    return render(request, 'index0.html', {})
def home(request):
    return render(request, 'index0.html', {})
def about(request):
    return render(request, 'about.html', {})
def photogallery(request):
    return render(request, 'photogallery.html', {})
def myaccount(request):
    return render(request, 'myaccount.html', {})
def register(request):
    return render(request, 'register.html', {})
def attraction(request):
    return render(request, 'attractions.html', {})
def ambassador(request):
    return HttpResponseRedirect("https://www.ambassadorbridge.com/")
def sports(request):
    return render(request, 'sports.html', {})