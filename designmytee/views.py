from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    response = render(request, 'designmytee/index.html')
    return response

def about(request):
    response = render(request, 'designmytee/about.html')
    return response
    
