from allauth.account.forms import SignupForm
from django import forms
from designmytee.models import Designer,Support_Request
 
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
    
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Support_Request
        fields = ('firstName','lastName','contactNumber','contactEmail','suggestionsOrFeedback')