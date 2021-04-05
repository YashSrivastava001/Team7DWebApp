from allauth.account.forms import SignupForm
from django import forms
from designmytee.models import Designer,Support_Request, Submission
from django.core.exceptions import ValidationError
 
class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    wins = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    participations = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    
    
    class Meta:
        model = Designer
        
    def save(self, request):  
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.wins = self.cleaned_data['wins']
        user.participations = self.cleaned_data['participations']
        user.save()
        Designer.objects.get_or_create(user=user,  participations=user.participations, wins=user.wins)[0]
        return user

class FeedbackForm(forms.ModelForm):
    firstName = forms.CharField(max_length=Support_Request.NAME_MAX_LENGTH,help_text="Please enter your first name:")
    lastName = forms.CharField(max_length=Support_Request.NAME_MAX_LENGTH, help_text="Please enter your last name:")
    contactNumber = forms.CharField(max_length=11, help_text="Please enter your phone number:")
    contactEmail = forms.EmailField(max_length=Support_Request.EMAIL_MAX_LENGTH, help_text="Please enter your email:")
    suggestionsOrFeedback = forms.CharField(max_length=Support_Request.SUGGESTIONS_FEEDBACK_MAX_LENGTH, help_text="Please enter your suggestion/query/feedback:")
    
    def clean_contactNumber(self):
        contactnum = self.cleaned_data['contactNumber']
        numlist = ['0','1','2','3','4','5','6','7','8','9']
        
        if len(contactnum) != 11:
            raise ValidationError('Error, not a valid phone number, length must be 11 and in the form: "07124282832"')
       
        for s in contactnum:
            if s not in numlist:
                raise ValidationError('Error, please enter a number in the form: "07124282832" ')
        return contactnum
    
    # Tests below check for invalid lengths of fields, but lengths are already constrained by input boxes, so no need to test these
    
    def clean_firstName(self):
        firstname = self.cleaned_data['firstName']
        
        if len(firstname) > 128:
            raise ValidationError('Error, firstname cannot be more than 128 characters')#
        
        return(firstname)
    def clean_lastName(self):
        lastname = self.cleaned_data['lastName']
        
        if len(lastname) > 128:
            raise ValidationError('Error, lastname cannot be more than 128 characters')

        return lastname
    
    def clean_email(self):
        email = self.cleaned_data['contactEmail']
        
        if len(email) > 200:
            raise ValidationError('Error, email cannot be more than 200 characters')
        
        return email
    def clean_suggestionsOrFeedback(self):
        suggestionsOrFeedback = self.cleaned_data['suggestionsOrFeedback']
        
        if len(suggestionsOrFeedback) > 500:
            raise ValidationError('Error, Feedback cannot be more than 500 characters')
            
        return suggestionsOrFeedback
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Support_Request
        fields = ('firstName','lastName','contactNumber','contactEmail','suggestionsOrFeedback')



class SubmissionForm(forms.ModelForm):
    designImage = forms.ImageField(help_text="Please upload your design:")
    submissionDescription = forms.CharField(max_length=Submission.DESCRIPTION_MAX_LENGTH,)
    votes = forms.IntegerField(widget=forms.HiddenInput(), initial=0, required=False)
    winner = forms.BooleanField(widget=forms.HiddenInput(), initial=False, required=False) 
    

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Submission
        fields = ('designImage','submissionDescription', 'competition', 'participant')
        widgets = {'competition': forms.HiddenInput(), 'participant': forms.HiddenInput()}