from allauth.account.forms import SignupForm
from django import forms
from .models import Profile,PhysicalAddresses

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    username = forms.CharField(max_length=30, label='Username')
    phone_number = forms.CharField(max_length=30, label='Phone Number')
    
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.phone_number = self.cleaned_data['phone_number']
        user.username = self.cleaned_data['username']
        user.save()
        return user


GENDER_CHOICES = (
    ('female', 'female'),
    ('male', 'male'),
    ('none', 'none')
)
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=('user','ip')
        widgets={
            'first_name':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'last_name':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'profile_picture':forms.FileInput(
                attrs={
                    'class':"form-control",
                }
            ),
            
            'gender':forms.Select(
                choices=GENDER_CHOICES,
                attrs={
                    'class':'form-control'
                }
            ),
            'tanggal_lahir':forms.DateInput(
                attrs={
                    'class': 'form-control', 
                    'type': 'date',
                }
            ),
            'phone_number':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
        }