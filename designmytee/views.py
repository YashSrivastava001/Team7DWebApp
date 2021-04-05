from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django. contrib import messages
from designmytee.models import Competition, Designer, Submission, ItemVideo, Vote
from django.template import RequestContext
from designmytee.forms import CustomSignupForm, FeedbackForm, SubmissionForm
from django.shortcuts import redirect
from django.contrib.auth import get_user
from django.shortcuts import get_object_or_404
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
    
    context_dict = {} 
    winningDesigners = []

    for competition in closed_competitions_list:
        
        # Checks if the lucky draw winner for the competition has already been decided, if it has not then use a random number generator to
        # determine the winner
<<<<<<< HEAD
        if competition.competitionWinner == None:
            competition_submissions = Submission.objects.filter(competition=competition)
            max_votes = 0
            winningSub = competition_submissions[0]
            for submission in competition_submissions:
                if submission.votes > max_votes:
                    max_votes = submission.votes
                    winningSub = submission
                    
            competition.competitionWinner = winningSub
=======
        
        winningDesigners.append(Designer.objects.get(user = competition.competitionWinner.participant))

>>>>>>> 18e5141108cc35595151c9a4c8cb99145ef1bd9b
        if competition.luckyDrawWinner == None:
            random_id = random.randint(1, len(all_designers))
            competition.luckyDrawWinner = Designer.objects.get(id=random_id).user
            
            competition.save(update_fields=["luckyDrawWinner"])
            

    context_dict['closed_competitions'] = closed_competitions_list

    context_dict['winningDesigners'] = winningDesigners
    print(context_dict['winningDesigners'])

    return render(request, 'designmytee/results.html', context = context_dict)

def competitions(request):
    
    end = date(2030, 12 , 12)
    start2 = date(2010, 12 , 12)
    start = date.today()
    
    context_dict = {}
    
    # below query set filters out competition that have not started yet, and competitions that are in voting stage
    
    participation_competitions = Competition.objects.filter(endDate__range=[start, end], startDate__range=[start2, start]).order_by('expiryDate')
    
    # below query set filters out competitons that have not started yet, and competitions that are in submission stage
    
    voting_competitions = Competition.objects.filter(endDate__range=[start2, start], expiryDate__range=[start, end]).order_by('expiryDate')

    featured_competition = Competition.objects.filter(expiryDate__range=[start, end], startDate__range=[start2, start]).order_by('expiryDate')[:1]
    
    context_dict['participation_competitions'] = participation_competitions
    context_dict['featured_competition'] = featured_competition
    context_dict['voting_competitions'] = voting_competitions

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
                participant = Designer.objects.get(user=request.user).user
                noOfSubmissions = Submission.objects.filter(competition=competition, participant=participant).count()
                if (noOfSubmissions < 1):
                    instance = form.save(commit=False)
                    instance.competition = competition
                    instance.participant = participant
                    instance.save()
                    return redirect('/designmytee/')
                else:
                    return redirect('/designmytee/competitions/')
            else:
                print(form.errors)


    except Competition.DoesNotExist:
        context_dict['competition'] = None
       

    # Go render the response and return it to the client.
    return render(request, 'designmytee/competition.html', context=context_dict)

def show_designer_profile(request, designer_slug):
    context_dict={}
    print(designer_slug)
    try:
        designer = Designer.objects.get(slug=designer_slug)
        context_dict['designer'] = designer

    except Designer.DoesNotExist:
        context_dict['designer'] = None

    print(context_dict)

    return render(request, 'designmytee/designerProfile.html', context=context_dict)




class VoteSubmissionView(View):
    def get(self, request):
        submission_id = request.GET['submission_id']
        try:
            submission = Submission.objects.get(id=int(submission_id))

        except Submission.DoesNotExist:
            return HttpResponse(-1)

        except Vote.DoesNotExist:
            return HttpResponse(-1)

        except ValueError:
            return HttpResponse(-1)
        
        user_voted = submission.voter.filter(user=request.user).exists()
        if not user_voted:
            Vote.objects.create(user = request.user, submission=submission)
            submission.votes = submission.votes + 1
            submission.save()
            return HttpResponse(submission.votes)
                
        if user_voted:
            messages.error(request, "You Have Already Voted For This Submission!!!")
            return redirect('/designmytee/')
        
