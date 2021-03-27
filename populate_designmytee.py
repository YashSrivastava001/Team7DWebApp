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
    
    python_Competitions = [
        {'competitionID': "81039102",
         'competitionDescription': 'Submit your favourite animal picture design!',
         'title': "Animals",
         'startDate': '2020-03-23',
         'endDate': '2020-05-22'
            },
        {'competitionID': "01928482",
         'competitionDescription': 'Submit your favourite TV show design!',
         'title': "TV shows",
         'startDate': '2020-04-23',
         'endDate': '2020-04-30'
            },
        {'competitionID': "62738492",
         'competitionDescription': 'Submit your favourite video game design!',
         'title': "video games",
         'startDate': '2021-04-23',
         'endDate': '2021-04-30'
            }
        ]
    
    python_Submissions = [
        {'votes': 12,
         'participant': python_Designers[3],
         'submissionDescription': 'Its a tiger, imagine a cat but like REALLY big',
         'designImage': "submission_images/test.jpg",
         'competition': python_Competitions[0]
         },
        {'votes': 22,
         'participant': python_Designers[1],
         'submissionDescription': 'puppy!',
         'designImage': "submission_images/dog.jpg",
         'competition': python_Competitions[0]
         },
        {'votes': 1,
         'participant': python_Designers[2],
         'submissionDescription': 'Is this google',
         'designImage': "submission_images/me.jpg",
         'competition': python_Competitions[2]
         },
        {'votes': 72,
         'participant': python_Designers[0],
         'submissionDescription': 'Idk its sitting funny what else do you want',
         'designImage': "submission_images/dog2.png",
         'competition': python_Competitions[0]
         }
        ]
    
    for Des in python_Designers:
        add_Designer(Des.get('name'), Des.get('userID'), Des.get('password'), Des.get('email'), Des.get('partcipations'))
        
    for Hos in python_Hosts:
        add_Host(Hos.get('name'), Hos.get('userID'), Hos.get('password'), Hos.get('email'), Hos.get('competitionsCreated'))
        
    for Comp in python_Competitions:
        add_Competition(Comp.get('competitionID'), Comp.get('competitionDescription'), Comp.get('title'), Comp.get('startDate'), Comp.get('endDate'))
        
    for Sub in python_Submissions:
        add_Submission(Sub.get('votes'), Sub.get('participant'), Sub.get('submissionDescription'), Sub.get('designImage'), Sub.get('competition'))
        
        
    
def add_Designer(name, userID, password, email, participations=0):
    d = Designer.objects.get_or_create(name=name, userID=userID, password=password, email=email)[0]
    d.participations = participations
    return d
    
def add_Host(name, userID, password, email, competitionsCreated=0):
    h = Host.objects.get_or_create(name=name, userID=userID, password=password, email=email)[0]
    h.competitionsCreated = competitionsCreated
    return h

def add_Competition(competitionID, competitionDescription, title, startDate, endDate):
    c = Competition.objects.get_or_create(competitionID=competitionID, competitionDescription=competitionDescription, title=title, startDate=startDate, endDate=endDate)[0]
    return c
        
def add_Submission(votes, participant, submissionDescription, designImage, competition):
    c = Competition.objects.filter(competitionID=competition.get('competitionID'))[0]
    d = Designer.objects.filter(name=participant.get('name'))[0]
    s = Submission.objects.get_or_create(votes=votes, participant=d, submissionDescription=submissionDescription, designImage=designImage, competition=c)[0]
    s.votes=votes
    return s

    
if __name__ == '__main__':
    print('Starting ratemytee population script...')
    populate()
    print('Population successful!')
        
        
        
        
        