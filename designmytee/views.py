from django.shortcuts import render
from django.http import HttpResponse
from designmytee.models import Competition
from django.template import RequestContext

# Create your views here.

def home(request):
    competitions_list = Competition.objects.all()
    context_dict = {}
    context_dict['competitions'] = competitions_list
    return render(request, 'designmytee/home.html', context = context_dict)

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


