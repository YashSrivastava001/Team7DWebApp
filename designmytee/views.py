from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'designmytee/home.html')

def about(request):
     return render(request, 'designmytee/about.html')
 
def help(request):
    return render(request, 'designmytee/help.html')

def myprofile(request):
     return render(request, 'designmytee/myprofile.html')

def results(request):
    return render(request, 'designmytee/results.html')

def competitions(request):
    return render(request, 'designmytee/competitions.html')


