from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField

# model used to store designer instances, uses a base user model from the standard django auth models, also has profile picture field,
# a participations field to store how many competitions the user has participated in and a slug field used to display other users profile

class Designer(models.Model):
    

    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, unique=True)
     
    picture = models.ImageField(upload_to='profile_images/', blank=True, default='images/homepage-cover.jpeg') # optional field
    participations = models.IntegerField(default=0, null=True)
    wins = models.IntegerField(default=0, null=True)

    slug = models.SlugField(unique=True, default=None)

    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.id)
        print(self.slug)
        super(Designer, self).save(*args, **kwargs)
    
    
# Model used to store instances of Competitions, contains title field for the competition title, a competitionDescription for an overview of the competition,
# a competitionImage attribute to store an image for the competiton, a start date representing when a competition is open for submissions, an end date
# for when the submissions should be closed and votes should be open, an expiryDate field for when the competition should be closed for votes. It also contains
# a luckyDrawWinner field to store a user instance of the user wins the lucky draw asepct and finally a competition winner field to store the user that won the competition

class Competition(models.Model):
    DESCRIPTION_MAX_LENGTH = 200
    COMPETITION_MAX_TITLE_LENGTH = 128
    
    title = models.CharField(max_length=COMPETITION_MAX_TITLE_LENGTH, default=None)
    competitionDescription = models.CharField(max_length=DESCRIPTION_MAX_LENGTH, default=None)
    competitionImage = models.ImageField(upload_to='competition_images/', blank=True) # optional field
    startDate = models.DateField()
    endDate = models.DateField()
    luckyDrawWinner = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, null=True, blank=True)
    
    expiryDate = models.DateField(default=None)
    competitionWinner = models.OneToOneField("Submission", related_name="competition_Winner", on_delete=models.CASCADE, default=None, unique=False, null=True) # Submission is in quotes as it is not defined yet

    
    slug = models.SlugField(unique=True, default=None)
    
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Competition, self).save(*args, **kwargs)
    

    class Meta:
        verbose_name_plural = 'competitions'

    def __str__(self):
        return self.title
    
    # Below functions are used for testing
    
    # checks the inupted competition instance, returns true if the start date is before the end date
    
    def start_date_before_end_date(self):
        return(self.startDate <= self.endDate)
    
    # checks the inputed competiton instance, returns true if the end date is before the expiry date
    
    def end_date_before_expiry_date(self):
        return(self.endDate <= self.expiryDate)
    
    # checks the inputed fields length is less than or equal to the inputed size
    
    def test_length(self, size, fieldToTest):
        return(len(fieldToTest) <= size)
    
# Submission is used to store an instance of a users submission, contants a designImage field that is used to store the image the user would like to submit for
# their entry, a submissionDescription which allows the user to input a short paragraph or so about their submission, a votes field to store how many votes the submission
# has, a winner field to store if the entry is a winner of the assosiated competiton, a partitipant field to store the user instance that submitted the submission
# and a competition field to store the competition that the submission is for

class Submission(models.Model):
    DESCRIPTION_MAX_LENGTH = 200
    designImage = models.ImageField(upload_to='Submission_images/', null=True, blank=True)
    submissionDescription = models.CharField(max_length=DESCRIPTION_MAX_LENGTH, default=None)
    votes = models.IntegerField(default=0)
    winner = models.BooleanField(default=False) 
    participant = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, null=True, blank=True)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, default=None, unique=False, null=True, blank=True) 
    
    def test_length(self, size, fieldToTest):
        return(len(fieldToTest) <= size)
    
# Support request field used to store the support or feedback request that are sent into the website through the help page, contains a firstName and lastName field
# for the user to enter their name, a contact number and contact email field for the user to enter their contact details and a suggestions or feedback field
# for the user to enter their support request

class Support_Request(models.Model):
    NAME_MAX_LENGTH = 128
    EMAIL_MAX_LENGTH = 200
    SUGGESTIONS_FEEDBACK_MAX_LENGTH = 500
    
    firstName = models.CharField(max_length=NAME_MAX_LENGTH)
    lastName = models.CharField(max_length=NAME_MAX_LENGTH)
    contactNumber = models.CharField(max_length=11)
    contactEmail = models.EmailField(max_length=EMAIL_MAX_LENGTH)
    suggestionsOrFeedback = models.CharField(max_length=SUGGESTIONS_FEEDBACK_MAX_LENGTH)
    
    def test_length(self, size, fieldToTest):
        return(len(fieldToTest) <= size)
    
# field used to store instances of videos to be displayed on the website

class ItemVideo(models.Model):
    video = EmbedVideoField()

# field used to store instances of votes that the user submits, used to make sure users can only vote once

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name='voter')
