from django.db import models
from django.contrib.auth.models import User

class Designer(models.Model):
     ID_MAX_LENGTH = 8
    
     user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, unique=True)
     
     picture = models.ImageField(upload_to='profile_images/', blank=True) # optional field
     participations = models.IntegerField(default=0, null=True)
     wins = models.IntegerField(default=0, null=True)
     luckyDrawWinner = models.BooleanField(default=False)
    
class Competition(models.Model):
    DESCRIPTION_MAX_LENGTH = 200
    COMPETITION_MAX_TITLE_LENGTH = 128
    
    title = models.CharField(max_length=COMPETITION_MAX_TITLE_LENGTH, default=None)
    competitionDescription = models.CharField(max_length=DESCRIPTION_MAX_LENGTH, default=None)
    competitionImage = models.ImageField(upload_to='competition_images/', blank=True) # optional field
    startDate = models.DateField()
    endDate = models.DateField()
    
    def start_date_before_end_date(self):
        return(self.startDate < self.endDate)
    
class Submission(models.Model):
    DESCRIPTION_MAX_LENGTH = 200
    
    designImage = models.ImageField(upload_to='Submission_images/')
    submissionDescription = models.CharField(max_length=DESCRIPTION_MAX_LENGTH, default=None)
    votes = models.IntegerField(default=0)
    winner = models.BooleanField(default=False) 
    participant = models.ForeignKey(Designer, on_delete=models.CASCADE, unique=False)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, default=None, unique=False) 

class Support_Request(models.Model):
    NAME_MAX_LENGTH = 128
    EMAIL_MAX_LENGTH = 200
    SUGGESTIONS_FEEDBACK_MAX_LENGTH = 500
    
    firstName = models.CharField(max_length=NAME_MAX_LENGTH)
    lastName = models.CharField(max_length=NAME_MAX_LENGTH)
    contactNumber = models.CharField(max_length=11)
    contactEmail = models.CharField(max_length=EMAIL_MAX_LENGTH)
    suggestionsOrFeedback = models.CharField(max_length=SUGGESTIONS_FEEDBACK_MAX_LENGTH)
    