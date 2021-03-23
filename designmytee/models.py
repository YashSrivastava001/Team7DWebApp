from django.db import models

# User class is an abstract class used for Designers and Hosts

class User(models.Model):
    NAME_AND_PASSWORD_MAX_LENGTH = 128
    USER_MAX_LENGTH = 8
    name = models.CharField(max_length=NAME_AND_PASSWORD_MAX_LENGTH)
    userID = models.CharField(max_length=USER_MAX_LENGTH, unique=True)
    password = models.CharField(max_length=NAME_AND_PASSWORD_MAX_LENGTH, unique=True)
    email = models.EmailField(unique=True)
    picture = models.ImageField(upload_to='profile_images/', blank=True)
    
    class Meta:
        abstract = True
    
class Designer(User):
    participations = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    luckyDrawWinner = models.BooleanField(default=False)
    
class Host(User):
    competitionsCreated = models.IntegerField(default=0)
    
class Competition(models.Model):
    COMPETITION_MAX_LENGTH = 8
    COMPETITION_MAX_TITLE_LENGTH = 128
    title = models.CharField(max_length=COMPETITION_MAX_TITLE_LENGTH, default=None)
    competitionID = models.CharField(max_length=COMPETITION_MAX_LENGTH)
    startDate = models.DateField()
    endDate = models.DateField()
    
class Submission(models.Model):
    designImage = models.ImageField(upload_to='Submission_images/')
    votes = models.IntegerField(default=0)
    winner = models.BooleanField(default=False)
    participant = models.OneToOneField(Designer, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, default=None)
