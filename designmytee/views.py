from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django. contrib import messages
from designmytee.models import Competition, Designer, Submission, ItemVideo, Vote

from django.template import RequestContext
from designmytee.forms import CustomSignupForm, FeedbackForm, SubmissionForm, UploadProfilePicForm
from django.shortcuts import redirect
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

    try:
        designer = Designer.objects.get(user=request.user)
        context_dict['designer'] = designer
        form = UploadProfilePicForm(instance = designer)
        context_dict['form'] = form

        if request.method == 'POST':
            form = UploadProfilePicForm(request.POST, request.FILES, instance=designer)
            if form.is_valid():
                form.save()
    except Designer.DoesNotExist:
        context_dict['designer'] = None

    return render(request, 'designmytee/myprofile.html', context=context_dict)

def results(request):
    
    # dates used to determine if a competition has already ended or not
    
    start = date(2010, 12 , 12)
    end = date.today()
    
    
    # below queryset only shows competitoons that have finished (the competitions end date is in the time frame provided)
    
    closed_competitions_list = Competition.objects.filter(expiryDate__range=[start, end]).order_by('endDate')
    
    context_dict = {} 
    winningDesigners = []

    for competition in closed_competitions_list:
        
        # Checks if the lucky draw winner for the competition has already been decided, if it has not then use a random number generator to
        # determine the winner

        if competition.competitionWinner == None:
            competition_submissions = Submission.objects.filter(competition=competition)
            
            # temp variables used to find the winner of the competition
            
            max_votes = 0
            winningSub = competition_submissions[0]
            for submission in competition_submissions:
                if submission.votes > max_votes:
                    max_votes = submission.votes
                    winningSub = submission
                    
            competition.competitionWinner = winningSub
            
            winningUser = winningSub.participant
            
            # gets the Designer instance from the winning user and increases the wins field by one, then saves
            
            winningUserDesigner = Designer.objects.get(user=winningUser)
            
            winningUserDesigner.wins = winningUserDesigner.wins + 1
            
            winningUserDesigner.save()
            
            # saves the new competition winner in the database
            
            competition.save(update_fields=["competitionWinner"])

        
        winningDesigners.append(Designer.objects.get(user = competition.competitionWinner.participant))
        
        # Checks if a lucky draw winner for the competition is present, if not generates a new one by generating a random number between 1 and the number of users inclusive,
        # then uses said number as an ID to choose the winner
        DesignersToUse = Submission.objects.filter(competition=competition)
        
        if competition.luckyDrawWinner == None:
            
            # Generates random number between 0 and the length of all the submiting designers -1 to select a random user who participted in the competition
            
            randomnum = random.randint(0, len(DesignersToUse) - 1)
            
            
            winner = DesignersToUse[randomnum].participant.id
            competition.luckyDrawWinner = Designer.objects.get(id=winner).user
            
            # saves the new lucky draw winner in the database
            
            competition.save(update_fields=["luckyDrawWinner"])
            
    # passes in the fields generated above into the context dictionary to display to the user        

    context_dict['closed_competitions'] = closed_competitions_list

    context_dict['winningDesigners'] = winningDesigners

    return render(request, 'designmytee/results.html', context = context_dict)

def competitions(request):
    
    # dates uses to determine what competitions to show to the user
    
    end = date(2030, 12 , 12)
    start2 = date(2010, 12 , 12)
    start = date.today()
    
    context_dict = {}
    
    # below query set filters the competitions to the ones that are in submission stage (competitons that are after the start date, but before the end date)
    
    participation_competitions = Competition.objects.filter(endDate__range=[start, end], startDate__range=[start2, start]).order_by('expiryDate')
    
    # below query set filters the competitions to the ones that are in voting stage (competitons that are after the start date, and after the end date but before the expiry date)
    
    voting_competitions = Competition.objects.filter(endDate__range=[start2, start], expiryDate__range=[start, end]).order_by('expiryDate')

    featured_competition = Competition.objects.filter(expiryDate__range=[start, end], startDate__range=[start2, start]).order_by('expiryDate')[:1]
    
    # above lists of competitons passed into seperate entries of the context dictionary
    
    context_dict['participation_competitions'] = participation_competitions
    
    context_dict['featured_competition'] = featured_competition
    
    context_dict['voting_competitions'] = voting_competitions

    return render(request, 'designmytee/competitions.html', context=context_dict)

def show_competition(request, competition_name_slug):
# Create a context dictionary which we can pass
# to the template rendering engine.
    context_dict = {}

    try:
        
        # gets a competition based on the competiton slug passed into view
    
        competition = Competition.objects.get(slug=competition_name_slug)
        context_dict['competition'] = competition
        
        # sets the voteOpen boolean value to either true or false, as it is used to control what elements the user can see
        # (If true, then the user cannot submit and only vote, if False then the user can submit but not vote)
        
        if competition.endDate < date.today():
            voteOpen = True
        elif competition.endDate >= date.today():
            voteOpen = False
        
        context_dict['voteOpen'] = voteOpen # VoteOpen value passed into context dictionary
        
        # submission list used to show submissions from the passed in competition to the user
        
        submission_list = Submission.objects.filter(competition=competition)
        
        context_dict['submissions'] = submission_list
        
        # passes in form for the user to fill in for a submission to the competition

        form = SubmissionForm
        context_dict['form'] = form
        
        # if the user is wanting to submit a submission to the competition, checks the users entered the information into the form correctly and saves the
        # users entry into the database

        if request.method == 'POST':
            form = SubmissionForm(request.POST , request.FILES)
            if form.is_valid():
                participant = Designer.objects.get(user=request.user).user
                noOfSubmissions = Submission.objects.filter(competition=competition, participant=participant).count()
                
                # gets the designer instance connected to the user and updates the participation counter by 1
                
                DesignerInstance = Designer.objects.get(user=participant)
                
                DesignerInstance.participations = DesignerInstance.participations + 1
                DesignerInstance.save()
                if (noOfSubmissions < 1):
                    instance = form.save(commit=False)
                    instance.competition = competition
                    instance.participant = participant
                    instance.save()
                    
                    return redirect('/designmytee/')
                else:
                    
                     # Once the users entry has been successfuly entered, redirect them to the competitions page
                    
                    return redirect('/designmytee/competitions/')
            else:
                print(form.errors)


    except Competition.DoesNotExist:
        context_dict['competition'] = None
       

    # Go render the response and return it to the client.
    return render(request, 'designmytee/competition.html', context=context_dict)

def show_designer_profile(request, designer_slug):
    context_dict={}
    
    # uses designer slug to select the designer profile to display to the user
    
    try:
        designer = Designer.objects.get(slug=designer_slug)
        context_dict['designer'] = designer

    except Designer.DoesNotExist:
        context_dict['designer'] = None

    return render(request, 'designmytee/designerProfile.html', context=context_dict)




class VoteSubmissionView(View):
    def get(self, request):
        
        # uses request to get the id of the submission
        
        submission_id = request.GET['submission_id']
        try:
            submission = Submission.objects.get(id=int(submission_id))

        except Submission.DoesNotExist:
            return HttpResponse(-1)

        except Vote.DoesNotExist:
            return HttpResponse(-1)

        except ValueError:
            return HttpResponse(-1)
        
        # If the user has not already voted for this submission, add the vote, if they have already voted for this submission then
        # show message to user saying they cannot vote for the same submission again
        
        user_voted = submission.voter.filter(user=request.user).exists()
        if not user_voted:
            Vote.objects.create(user = request.user, submission=submission)
            submission.votes = submission.votes + 1
            submission.save()
            return HttpResponse(submission.votes)
                
        if user_voted:
            messages.error(request, "You Have Already Voted For This Submission!!!")
            return redirect('/designmytee/')
        

