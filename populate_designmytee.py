import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'Team7DWebApp.settings')

import django
django.setup()
from designmytee.models import Designer, Submission, Competition, Support_Request
from django.contrib.auth.models import User

def populate():
    
    python_Designers = [
        {'first_name': 'John',
         'last_name': 'Thomas',
         'username': 'John212',
         'password':'badPassword123',
         'email':'JohnJones@fakemail.com',
         'participations':52,
         'picture': 'profile_images/profile_1.jpg',
         'wins': 22},
        {'first_name': 'Simon',
         'last_name': 'Peterson',
         'username': 'Simon1212',
         'password':'goodPassword-12345',
         'email':'SimmySimon@realmail.co.uk',
         'participations':9,
         'wins': 2},
        {'first_name': 'Malinda',
         'last_name': 'Robberts',
         'username': 'boom673',
         'password':'password',
         'participations': 321,
         'picture': 'profile_images/profile_3.jpg',
         'email':'mysonsetthisup@testmail.com'},
        {'first_name': 'Sven',
         'last_name': 'Robberts',
         'username': 'Ö7',
         'password':'WhereAmI',
         'email':'Ö@fakemail.com',
         'participations':812,
         'wins': 111},
        {'first_name': 'Paul',
         'last_name': 'Byron',
         'username': 'PaulJog',
         'password':'Test1234',
         'email':'Paul@fakemail.com',
         'participations':221,
         'wins': 32},
        {'first_name': 'Tim',
         'last_name': 'Thomas',
         'username': 'timtom',
         'password':'GoodPassword_99',
         'email':'timetamtom@testmail.com',
         'participations':88,},
        {'first_name': 'Userson',
         'last_name': 'Samson',
         'username': 'user444',
         'password':'testpassword',
         'email':'useremail@fakemail.com',
         'participations':3,
         'wins': 2},
        {'first_name': 'Phil',
         'last_name': 'Pjyotr',
         'username': 'designer234',
         'password':'pleaseDontSteal',
         'email':'designer234@testmail.com',
         'participations':2212,
         'wins': 1111},
        ]
    
    python_Hosts = [
        {'first_name': 'bob',
         'last_name': 'Wilbur',
         'username': 'bob1',
         'password': 'WindowCleaner',
         'email': 'LookingForCat@petmail.com'},
        {'first_name': 'Scott',
         'last_name': 'Thomas',
         'username': 'hostUser',
         'password': 'grapeSoda',
         'email': 'sodapoda@petmail.com',}
        ]
    
    python_Competitions = [
        {
         'competitionDescription': 'Submit your favourite animal picture design!',
         'competitionImage': 'competition_images/competition_1.jpg',
         'title': "Animals",
         'startDate': '2021-04-02',
         'endDate': '2021-07-22',
         'expiryDate': '2021-08-22'
            },
        {
         'competitionDescription': 'Submit your favourite TV show design!',
         'competitionImage': 'competition_images/competition_2.jpg',
         'title': "TV shows",
         'startDate': '2020-12-23',
         'endDate': '2021-02-28',
         'expiryDate': '2021-03-30'
            },
        {
         'competitionDescription': 'Submit your favourite video game design!',
         'competitionImage': 'competition_images/competition_3.jpg',
         'title': "video games",
         'startDate': '2021-02-27',
         'endDate': '2021-05-13',
         'expiryDate': '2021-06-14'
            },
        {
         'competitionDescription': 'Submit your favourite city picture design!',
         'competitionImage': 'competition_images/competition_4.jpg',
         'title': "Cities",
         'startDate': '2021-01-13',
         'endDate': '2021-04-01',
         'expiryDate': '2021-05-01',
            },
        {
         'competitionDescription': 'Submit your favourite space themed design!',
         'competitionImage': 'competition_images/competition_5.jpg',
         'title': "Space",
         'startDate': '2020-11-03',
         'endDate': '2021-02-28',
         'expiryDate': '2021-03-28'
            },
        {
         'competitionDescription': 'Submit your favourite country themed design!',
         'competitionImage': 'competition_images/competition_6.jpg',
         'title': "Countries",
         'startDate': '2021-08-23',
         'endDate': '2021-09-22',
         'expiryDate': '2021-10-22'
            }
        
        ]
    
    python_Submissions = [
        {'votes': 12,
         'participant': 4,
         'submissionDescription': 'Its a tiger, imagine a cat but like REALLY big',
         'designImage': "submission_images/submission_1_4.jpg",
         'competition': 1
         },
        {'votes': 22,
         'participant': 2,
         'submissionDescription': 'puppy!',
         'designImage': "submission_images/submission_1_2.jpg",
         'competition': 1
         },
        {'votes': 1,
         'participant': 3,
         'submissionDescription': 'Is this google',
         'designImage': "submission_images/submission_1_3.jpg",
         'competition': 1
         },
        {'votes': 72,
         'participant': 1,
         'submissionDescription': 'Idk its sitting funny what else do you want',
         'designImage': "submission_images/submission_1_1.png",
         'competition': 1
         },
        {'votes': 32,
         'participant': 5,
         'submissionDescription': 'My favourite TV show! made the design myself....',
         'designImage': "submission_images/submission_2_5.jpg",
         'competition': 2
         },
        {'votes': 22,
         'participant': 6,
         'submissionDescription': 'The best Netflix series! cant wait for the next season!',
         'designImage': "submission_images/submission_2_6.png",
         'competition': 2
         },
        {'votes': 321,
         'participant': 7,
         'submissionDescription': 'Greatest video game character of all time!',
         'designImage': "submission_images/submission_3_7.jpg",
         'competition': 3
         },
        {'votes': 222,
         'participant': 8,
         'submissionDescription': 'The most popular video game of all time! I made this using photoshop',
         'designImage': "submission_images/submission_3_8.jpeg",
         'competition': 3
         },
        {'votes': 22,
         'participant': 5,
         'submissionDescription': 'This is my home city! I love it very much',
         'designImage': "submission_images/submission_4_5.jpg",
         'competition': 4
         },
        {'votes': 262,
         'participant': 3,
         'submissionDescription': 'I visited here last year... it was amazing!',
         'designImage': "submission_images/submission_4_3.jpg",
         'competition': 4,
         'winner': True
         },
        {'votes': 421,
         'participant': 1,
         'submissionDescription': 'I love space! I have always dreamed of visiting the moon!',
         'designImage': "submission_images/submission_5_1.jpg",
         'competition': 5
         },
        {'votes': 174,
         'participant': 6,
         'submissionDescription': 'FOOD IN SPACE!!!!!!',
         'designImage': "submission_images/submission_5_6.jpg",
         'competition': 5,
         'winner': True
         },
        {'votes': 7,
         'participant': 2,
         'submissionDescription': 'I visited here last year, I would love to go again! it looks lovely on the map!',
         'designImage': "submission_images/submission_6_2.jpg",
         'competition': 6
         },
        {'votes': 22,
         'participant': 4,
         'submissionDescription': 'Austrailia is great, what a massive country!',
         'designImage': "submission_images/submission_6_4.jpg",
         'competition': 6
         },
        ]
    
    Feedback_Submissions = [
        {'firstName': 'Tim',
         'lastName': 'Higgins',
         'contactNumber': '07919421023',
         'contactEmail': 'LookingForDog@petmail.com',
         'suggestionsOrFeedback' : 'I enjoy using this site, but the site needs better moderation, somebody stole my work!'},
        {'firstName': 'Sam',
         'lastName': 'Chandler',
         'contactNumber': '07911921023',
         'contactEmail': 'LookingForBeaver@petmail.com',
         'suggestionsOrFeedback' : 'It would be nice to have a community spotlight section, maybe with a submission of the week by highest votes?'},
        {'firstName': 'Sam',
         'lastName': 'John',
         'contactNumber': '07817261023',
         'contactEmail': 'LookingForMouse@testmail.com',
         'suggestionsOrFeedback' : 'I would like to recieve more clarity on whats happening to my data'},
        ]
    
    for Des in python_Designers:
        add_Designer( Des.get('username'), Des.get('first_name'), Des.get('last_name'), Des.get('password'), Des.get('email'), Des.get('picture'), Des.get('participations'), Des.get('wins'))
        
    for Hos in python_Hosts:
        add_Host(Hos.get('username'), Hos.get('first_name'), Hos.get('last_name'), Hos.get('password'), Hos.get('email'))
        
    for Comp in python_Competitions:
        add_Competition(Comp.get('competitionDescription'), Comp.get('competitionImage'), Comp.get('title'), Comp.get('startDate'), Comp.get('endDate'), Comp.get('expiryDate'))
        
    for Sub in python_Submissions:
        add_Submission(Sub.get('participant'), Sub.get('submissionDescription'), Sub.get('designImage'), Sub.get('competition'), Sub.get('votes'),Sub.get('winner'))
    
    for Fed in Feedback_Submissions:
        add_Feedback(Fed.get('firstName'), Fed.get('lastName'), Fed.get('contactNumber'), Fed.get('contactEmail'), Fed.get('suggestionsOrFeedback'))
        
def add_Designer(name, firstName, lastName, password, email, picture=None, participations=0, wins=0):
    if wins == None:
        wins = 0
    if participations == None:
        wins = 0
        
    
    u = User.objects.create(username=name,  email=email, first_name=firstName, last_name=lastName)
    u.set_password(password)
    u.save()

    d = Designer.objects.get_or_create(user=u, picture=picture, participations=participations, wins=wins)[0]

    return d
    
def add_Host(name, firstName, lastName, password, email):
    u = User.objects.create(username=name, email=email, first_name=firstName, last_name=lastName, is_superuser=True, is_staff=True)
    u.set_password(password)
    u.save()
    
    return u

def add_Competition(competitionDescription, competitionImage, title, startDate, endDate, expiryDate):
    c = Competition.objects.get_or_create(competitionDescription=competitionDescription, competitionImage=competitionImage, title=title, startDate=startDate, endDate=endDate, expiryDate=expiryDate)[0]
    return c
        
def add_Submission(participant, submissionDescription, designImage, competition, votes=0, winner=False):
    if votes == None:
        votes = 0
    c = Competition.objects.get(id=competition)
    d = Designer.objects.get(id=participant)
    
    s = Submission.objects.get_or_create(votes=votes, participant=d, submissionDescription=submissionDescription, designImage=designImage, competition=c)[0]
    s.votes=votes
    
    if winner == True:
        Competition.objects.filter(id=competition).update(competitionWinner=s)
        
    return s

def add_Feedback(firstName, lastName, contactNumber, contactEmail, suggestionsOrFeedback):
    f = Support_Request.objects.get_or_create(firstName=firstName, lastName=lastName, contactNumber=contactNumber, contactEmail=contactEmail, suggestionsOrFeedback=suggestionsOrFeedback)
    return f
    
if __name__ == '__main__':
    print('Starting designmytee population script... this may take a second or two...')
    populate()
    print('Population successful!')
        
        
        
        
        