from allauth.account.forms import SignupForm
from django import forms
from designmytee.models import Designer
 
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
        d = Designer.objects.get_or_create(user=user,  participations=user.participations, wins=user.wins)[0]
        return user
