from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'designmytee/home.html')

def about(request):
     return render(request, 'designmytee/about.html')
 
def help(request):
    return render(request, 'designmytee/help.html')

def signin(request):
     return render(request, 'designmytee/signin.html')

def results(request):
    winners_list = Designer.objects.all()
    context_dict = {}
    context_dict['Winners'] = winners_list
    return render(request, 'designmytee/results.html', context = context_dict)

def competitions(request):
    return render(request, 'designmytee/competitions.html')


