from django.shortcuts import render
from django.http import HttpResponse
from designmytee.models import Competition, Designer
from django.template import RequestContext
from designmytee.forms import CustomSignupForm
from django.shortcuts import redirect
from django.contrib.auth import get_user

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
    context_dict = {}
    designers_list = Designer.objects.all()
    context_dict['designers'] = designers_list
    return render(request, 'designmytee/myprofile.html', context=context_dict)

def results(request):
    return render(request, 'designmytee/results.html')

def competitions(request):
    competitions_list = Competition.objects.all()
    context_dict = {}
    context_dict['competitions'] = competitions_list
    return render(request, 'designmytee/competitions.html', context=context_dict)


