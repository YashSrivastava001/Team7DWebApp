from django.test import TestCase
from designmytee.models import  Designer, Submission, Competition, Support_Request 
from populate_designmytee import populate
from designmytee.forms import FeedbackForm, CustomSignupForm, SubmissionForm

import os

# Various tests for the Models, forms and views, run "python manage.py test" to run all tests.
# Populate function from populate_designmytee is frequently used to create test databases for each set of tests, this may cause the tests
# to take longer as the populate function needs ~4 seconds to run each time

class DesignerTests(TestCase):
    
    print("Starting tests, this may take a short while!...")
    
    @classmethod
    def setUpTestData(cls):
        populate()

    def test_user_connected_to_designer(self):
        for d in Designer.objects.all():
            self.assertTrue(d.user != None, "Error, Designer instance exists with no user, please check user: " + str(d.id))
    
    def test_user_instances_contain_correct_fields(self):
        for d in Designer.objects.all():
            self.assertTrue(d.user.first_name != None, "Error, Designer intances user has no firstname, check user: " + str(d.id))
            self.assertTrue(d.user.last_name != None, "Error, Designer intances user has no lastname, check user: " + str(d.id))
            self.assertTrue(d.user.username != None, "Error, Designer intances user has no username, check user: " + str(d.id))
            self.assertTrue(d.user.password != None, "Error, Designer intances user has no password, check user: " + str(d.id))
            
    def test_category_image_directory_is_in_place(self):
        cwd = os.getcwd()
        profileDirectory = os.path.join(cwd, 'Media\profile_images')
        self.assertTrue(os.path.isdir(profileDirectory), "Error, profile_images folder not in media directory")
        
    def test_category_images_folder_not_empty(self):
        cwd = os.getcwd()
        profileDirectory = os.path.join(cwd, 'Media\profile_images')
        self.assertTrue(len(os.listdir(profileDirectory)) != 0, "Error, no images are stored in profile_images folder")
        
    def test_wins_and_participations_not_zero(self):
        for d in Designer.objects.all():
            self.assertTrue(d.wins >= 0, "Error, Designer instance exists with either no default wins or an invalid wins count, see user: " + str(d.id))
            self.assertTrue(d.participations >= 0, "Error, Designer instance exists with either no default participations or an invalid participation count, see user: " + str(d.id))
            
    def test_wins_not_more_than_participations(self):
        for d in Designer.objects.all():
            self.assertTrue(d.wins <= d.participations, "Error, designer wins are more than participations, check user: " + str(d.id))
        
class CompetitionTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        populate()
        

    def test_lengths_are_set_correctly(self):
        for c in Competition.objects.all():
            maxLength = c._meta.get_field('title').max_length
            self.assertEqual(maxLength, 128, "Error, Length value not correctly set in model, please check model max length value for title")
            maxLength = c._meta.get_field('competitionDescription').max_length
            self.assertEqual(maxLength, 200, "Error, Length value not correctly set in model, please check model max length value for competitionDescription")
            
    def test_category_image_directory_is_in_place(self):
        cwd = os.getcwd()
        competitionDirectory = os.path.join(cwd, 'Media\competition_images')
        self.assertTrue(os.path.isdir(competitionDirectory), "Error, competition_images folder not in media directory")
        
    def test_category_images_folder_not_empty(self):
        cwd = os.getcwd()
        competitionDirectory = os.path.join(cwd, 'Media\competition_images')
        self.assertTrue(len(os.listdir(competitionDirectory)) != 0, "Error, no images are stored in competition_images folder")
    
    def test_start_date_is_before_end_date(self):
        
        for c in Competition.objects.all():
            self.assertIs(c.start_date_before_end_date(), True, "Error, Start date is after end date, object id: " + str(c.id))
            
    def test_end_date_is_before_expiry_date(self):
        
        for c in Competition.objects.all():
            self.assertIs(c.end_date_before_expiry_date(), True, "Error, End date is after Expiry date, object id: " + str(c.id))
        
    def test_lengths_are_adheared_to(self):
        
        for c in Competition.objects.all():
            self.assertIs(c.test_length(fieldToTest=c.title, size=128), True, "Error, object title has an invalid size, object id: " + str(c.id))
            self.assertIs(c.test_length(fieldToTest=c.competitionDescription, size=200), True, "Error, object competitionDescription has an invalid size, object id: " + str(c.id))
            
class SubmissonTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        populate()
        
    def test_submission_image_directory_is_in_place(self):
        cwd = os.getcwd()
        submissionDirectory = os.path.join(cwd, 'Media\submission_images')
        self.assertTrue(os.path.isdir(submissionDirectory), "Error, submission_images folder not in media directory")
        
    def test_category_images_folder_not_empty(self):
        cwd = os.getcwd()
        submissionDirectory = os.path.join(cwd, 'Media\submission_images')
        self.assertTrue(len(os.listdir(submissionDirectory)) != 0, "Error, no images are stored in submission_images folder")
        
    def test_lengths_are_set_correctly(self):
        for s in Submission.objects.all():
            maxLength = s._meta.get_field('submissionDescription').max_length
            self.assertEqual(maxLength, 200, "Error, Length value not correctly set in model, please check model max length value for submissionDescription")
            
    def test_lengths_are_adheared_to(self):
        
        for s in Submission.objects.all():
            self.assertIs(s.test_length(fieldToTest=s.submissionDescription, size=200), True, "Error, object submissionDescription has an invalid size, object id: " + str(s.id))
            
    def test_participant_connected_to_submission(self):
        for s in Submission.objects.all():
            self.assertTrue(s.participant != None, "Error, Submission instance exists with no participant, please check user: " + str(s.id))
            
    def test_Competition_connected_to_submission(self):
        for s in Submission.objects.all():
            self.assertTrue(s.competition != None, "Error, Submission instance exists with no competition, please check user: " + str(s.id))
            
    def test_votes_not_zero(self):
        for s in Submission.objects.all():
            self.assertTrue(s.votes >= 0, "Error, Submission instance exists with either no default votes or an invalid votes count, see user: " + str(s.id))
            
class FeedbackTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        populate()
        
    def test_lengths_are_set_correctly(self):
        for f in Support_Request.objects.all():
            maxLength = f._meta.get_field('firstName').max_length
            self.assertEqual(maxLength, 128, "Error, Length value not correctly set in model, please check model max length value for firstname")
            maxLength = f._meta.get_field('lastName').max_length
            self.assertEqual(maxLength, 128, "Error, Length value not correctly set in model, please check model max length value for lastname")
            maxLength = f._meta.get_field('contactNumber').max_length
            self.assertEqual(maxLength, 11, "Error, Length value not correctly set in model, please check model max length value for contactnumber")
            maxLength = f._meta.get_field('contactEmail').max_length
            self.assertEqual(maxLength, 200, "Error, Length value not correctly set in model, please check model max length value for contactEmail")
            maxLength = f._meta.get_field('suggestionsOrFeedback').max_length
            self.assertEqual(maxLength, 500, "Error, Length value not correctly set in model, please check model max length value")
            
    def test_lengths_are_adheared_to(self):
        
        for f in Support_Request.objects.all():
            self.assertIs(f.test_length(fieldToTest=f.firstName, size=128), True, "Error, object firstname has an invalid size, object id: " + str(f.id))
            self.assertIs(f.test_length(fieldToTest=f.lastName, size=128), True, "Error, object lastname has an invalid size, object id: " + str(f.id))
            self.assertIs(f.test_length(fieldToTest=f.contactNumber, size=11), True, "Error, object contactNumber has an invalid size, object id: " + str(f.id))
            self.assertIs(f.test_length(fieldToTest=f.contactEmail, size=200), True, "Error, object contactEmail has an invalid size, object id: " + str(f.id))
            self.assertIs(f.test_length(fieldToTest=f.suggestionsOrFeedback, size=500), True, "Error, object suggestionsOrFeedback has an invalid size, object id: " + str(f.id))
            
class FormTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        populate()
        
    # checks that feedback and submission form can correctly detect an invalid input
    
    def test_feedback_form_detects_wrong_contact_number(self):
        form = FeedbackForm(data={'contactNumber': "08217482"})
        self.assertEqual(form.errors['contactNumber'], ['Error, not a valid phone number, length must be 11 and in the form: "07124282832"'], "Error, feedback form does not correctly identify phone numbers of incorrect length")
        form = FeedbackForm(data={'contactNumber': "8274h17f821"})
        self.assertEqual(form.errors['contactNumber'], ['Error, please enter a number in the form: "07124282832" '], "Error, feedback form does not correctly identify non-number input for contact number")
        
    def test_feedback_form_help_text(self):
        form = FeedbackForm()
        self.assertEqual(form.fields['firstName'].help_text, "Please enter your first name:", "Error, feedback form help text for firstname is invalid")
        self.assertEqual(form.fields['lastName'].help_text, "Please enter your last name:","Error, feedback form help text for lastname is invalid")
        self.assertEqual(form.fields['contactNumber'].help_text, "Please enter your phone number:", "Error, feedback form help text for contactNumber is invalid")
        self.assertEqual(form.fields['contactEmail'].help_text, "Please enter your email:", "Error, feedback form help text for contactEmail is invalid")
        self.assertEqual(form.fields['suggestionsOrFeedback'].help_text, "Please enter your suggestion/query/feedback:", "Error, feedback form help text for suggestionsOrFeedback is invalid")
        
    def test_Signup_form_lable_text(self):
        form = CustomSignupForm()
        self.assertEqual(form.fields['first_name'].label, 'First Name', "Error, Sign up form label text for first_name is invalid")
        self.assertEqual(form.fields['last_name'].label, 'Last Name', "Error, Sign up form label text for last_name is invalid")
        
class ViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        populate()
        
    def test__view_urls_at_correct_area(self):
        response = self.client.get('/designmytee/about/')
        self.assertEqual(response.status_code, 200, "Error, about response not at correct area")
        
        response = self.client.get('/designmytee/results/')
        self.assertEqual(response.status_code, 200, "Error, results response not at correct area")
        
        response = self.client.get('/designmytee/')
        self.assertEqual(response.status_code, 200, "Error, home response not at correct area")
        
        response = self.client.get('/designmytee/help/')
        self.assertEqual(response.status_code, 200, "Error, help response not at correct area")
        
        response = self.client.get('/designmytee/myprofile/')
        self.assertEqual(response.status_code, 200, "Error, myprofile response not at correct area")
        
        for competition in Competition.objects.all():
            
            response = self.client.get('/designmytee/competition/' + competition.slug + "/")
            self.assertEqual(response.status_code, 200, "Error, competition response not at correct area")
        
        response = self.client.get('/designmytee/competitions/')
        self.assertEqual(response.status_code, 200, "Error, competitions response not at correct area")
        
        response = self.client.get('/designmytee/login/')
        self.assertEqual(response.status_code, 200, "Error, login response not at correct area")
        
        response = self.client.get('/designmytee/signup/')
        self.assertEqual(response.status_code, 200, "Error, signup response not at correct area")
        
        response = self.client.get('/designmytee/password/reset/')
        self.assertEqual(response.status_code, 200, "Error, password reset response not at correct area")
        
        
        
        