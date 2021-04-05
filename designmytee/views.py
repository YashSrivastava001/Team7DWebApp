from django.shortcuts import render
from django.http import HttpResponse
from designmytee.models import Competition, Designer, Submission, ItemVideo
from django.template import RequestContext
from designmytee.forms import CustomSignupForm, FeedbackForm, SubmissionForm
from django.shortcuts import redirect
from django.contrib.auth import get_user
from datetime import date
import random

# Create your views here.

def home(request):
    end = date(2030, 12 , 12)
    start2 = date(2010, 12 , 12)
    start = date.today()
    
    # below query set filters out competition that have not started yet, and competitions that have finished (closed for voting and submissions)
    # and filters them by date (highest first, so the competitions closest to closing) and shows the top 3
    
    competitions_list = Competition.objects.filter(expiryDate__range=[start, end], startDate__range=[start2, start]).order_by('expiryDate')[:3]
    context_dict = {}
    context_dict['competitions'] = competitions_list
    return render(request, 'designmytee/home.html', context = context_dict)

def about(request):
    context_dict = {}
    videos = ItemVideo.objects.all()
    for video in videos:
        print("test")
    context_dict["item_video"] = videos
    return render(request, 'designmytee/about.html', context = context_dict)
 
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
    # The designer profile to show is filtered out in the HTML
    
    designers_list = Designer.objects.all()
    context_dict['designers'] = designers_list
    return render(request, 'designmytee/myprofile.html', context=context_dict)

def results(request):
    
    # dates used to determine if a competition has already ended or not
    
    start = date(2010, 12 , 12)
    end = date.today()
    
    
    # below queryset only shows competitoons that have finished (the competitions end date is in the time frame provided)
    
    closed_competitions_list = Competition.objects.filter(expiryDate__range=[start, end]).order_by('endDate')
    
    all_designers = Designer.objects.all()
    
    for competition in closed_competitions_list:
        
        # Checks if the lucky draw winner for the competition has already been decided, if it has not then use a random number generator to
        # determine the winner
        
        if competition.luckyDrawWinner == None:
            random_id = random.randint(1, len(all_designers))
            competition.luckyDrawWinner = Designer.objects.get(id=random_id).user
            
            competition.save(update_fields=["luckyDrawWinner"])
            
    context_dict = {}
    context_dict['closed_competitions'] = closed_competitions_list

    return render(request, 'designmytee/results.html', context = context_dict)

def competitions(request):
    
    end = date(2030, 12 , 12)
    start2 = date(2010, 12 , 12)
    start = date.today()
    
    context_dict = {}
    
    # below query set filters out competition that have not started yet, and competitions that have finished (closed for voting and submissions)
    
    competitions_list = Competition.objects.filter(expiryDate__range=[start, end], startDate__range=[start2, start]).order_by('expiryDate')
    
    context_dict['competitions'] = competitions_list
    return render(request, 'designmytee/competitions.html', context=context_dict)

def show_competition(request, competition_name_slug):
# Create a context dictionary which we can pass
# to the template rendering engine.
    context_dict = {}

    try:
    
        competition = Competition.objects.get(slug=competition_name_slug)
       
        
        context_dict['competition'] = competition
        
        # sets the voteOpen boolean value to either true or false, as it is used to control what elements the user can see
        # (If true, then the user cannot submit and only vote, if False then the user can submit but not vote)
        
        if competition.endDate < date.today():
            voteOpen = True
        elif competition.endDate >= date.today():
            voteOpen = False
            
        context_dict['voteOpen'] = voteOpen
        submission_list = Submission.objects.filter(competition=competition)

        context_dict['submissions'] = submission_list
        

        form = SubmissionForm

        

        context_dict['form'] = form

        if request.method == 'POST':
            
            form = SubmissionForm(request.POST , request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.competition = competition
                instance.participant = request.user
                instance.save()

               
                return redirect('/designmytee/')
            else:
                print(form.errors)


    except Competition.DoesNotExist:
        context_dict['competition'] = None
       

    # Go render the response and return it to the client.
    return render(request, 'designmytee/competition.html', context=context_dict)

