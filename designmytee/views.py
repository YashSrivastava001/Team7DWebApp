from django.shortcuts import render
from django.http import HttpResponse
from designmytee.models import Competition, Designer, Submission
from django.template import RequestContext
from designmytee.forms import CustomSignupForm, FeedbackForm
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
    form = FeedbackForm()
    
       # A HTTP POST?
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            # Now that the category is saved, we could confirm this.
            # For now, just redirect the user block to the index view.
            return redirect('/designmytee/')
        else:
            # The supplied form contained errors -
            # just print them to the terminal.
            print(form.errors)
    
    # Will handle the bad form, new form, or no form supplied cases.
    # Render the form with error messages (if any).
    return render(request, 'designmytee/help.html', {'form': form})

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

def show_competition(request, competition_name_slug):
# Create a context dictionary which we can pass
# to the template rendering engine.
    context_dict = {}

    try:
    
        competition = Competition.objects.get(slug=competition_name_slug)
       
        
        context_dict['competition'] = competition

        submission_list = Submission.objects.filter(competition=competition)

        context_dict['submissions'] = submission_list

    except Competition.DoesNotExist:
        context_dict['competition'] = None
       

    # Go render the response and return it to the client.
    return render(request, 'designmytee/competition.html', context=context_dict)

