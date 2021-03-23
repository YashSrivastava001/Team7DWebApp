import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'Team7DWebApp.settings')

import django
django.setup()
from designmytee.models import Host, Designer, Submission, Competition

def populate():
    
    python_Designers = [
        {'name': 'John',
         'userID':'64273894',
         'password':'badPassword123',
         'email':'JohnJones@fakemail.com',
         'participations':52,
         'wins': 22},
        {'name': 'Simon',
         'userID':'98271642',
         'password':'goodPassword-12345',
         'email':'SimmySimon@realmail.co.uk',
         'participations':9,
         'wins': 2},
        {'name': 'boom',
         'userID':'09182736',
         'password':'password',
         'email':'mysonsetthisup@testmail.com'},
        {'name': 'Ö',
         'userID':'22222222',
         'password':'WhereAmI',
         'email':'Ö@fakemail.com',
         'participations':321,
         'wins': 111},
        ]
    
    python_Hosts = [
        {'name': 'bob',
         'userID':'WhereIsMyCat',
         'password': 'WindowCleaner',
         'email': 'LookingForCat@petmail.com',
         'competitionsCreated': 24}
        ]
    
    python_Submissions = [
        {'votes': 12,
         'participant': python_Designers[3],
         'designImage': "submission_images/test.jpg"}
        ]
    
    python_Competitions = [
        {'competitionID': "81039102",
         'startDate': '2020-03-23',
         'endDate': '2020-05-22'
            }
        ]
    
    for Des in python_Designers:
        add_Designer(Des.get('name'), Des.get('userID'), Des.get('password'), Des.get('email'), Des.get('partcipations'))
        
    for Hos in python_Hosts:
        add_Host(Hos.get('name'), Hos.get('userID'), Hos.get('password'), Hos.get('email'), Hos.get('competitionsCreated'))
        
    for Sub in python_Submissions:
        add_Submission(Sub.get('votes'), Sub.get('participant'), Sub.get('designImage'))
        
    for Comp in python_Competitions:
        add_Competition(Comp.get('competitionID'), Comp.get('startDate'), Comp.get('endDate'))
        
        
    
    
def add_Designer(name, userID, password, email, participations=0):
    d = Designer.objects.get_or_create(name=name, userID=userID, password=password, email=email)[0]
    d.participations = participations
    return d
    
def add_Host(name, userID, password, email, competitionsCreated=0):
    h = Host.objects.get_or_create(name=name, userID=userID, password=password, email=email)[0]
    h.competitionsCreated = competitionsCreated
    return h
        
def add_Submission(votes, participant, designImage):
    d = Designer.objects.filter(name=participant.get('name'))[0]
    s = Submission.objects.get_or_create(participant=d, designImage=designImage)[0]
    s.votes=votes
    return s
        
def add_Competition(competitionID, startDate, endDate):
    c = Competition.objects.get_or_create(competitionID=competitionID, startDate=startDate, endDate=endDate)[0]
    return c
    
if __name__ == '__main__':
    print('Starting ratemytee population script...')
    populate()
    print('Population successful!')
        
        
        
        
        