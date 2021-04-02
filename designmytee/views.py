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

def show_competition(request, competition_name_slug):
# Create a context dictionary which we can pass
# to the template rendering engine.
    context_dict = {}

    try:
    
        competition = Competition.objects.get(slug=competition_name_slug)
       
        
        context_dict['competition'] = competition

    except Competition.DoesNotExist:
        context_dict['competition'] = None
       

    # Go render the response and return it to the client.
    return render(request, 'designmytee/competition.html', context=context_dict)


