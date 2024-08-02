from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from multihospital_app.models import Hospitalavail,HospitalRequest,HospitalDetail

class CustomUserCreationForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control p-2','placeholder': 'Hospital Name'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Hospital email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Enter Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Enter Confirm Password'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Hospital Name'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )

class HospitalavailForm(forms.ModelForm):    
    class Meta:
        model = Hospitalavail
        fields = ['name', 'availability', 'info','availabilitylist','image']
        widgets = {
            
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Available Type Name'}),
            'availability': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'How Much Available'}),
            'info': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter Available info'}),
            'availabilitylist': forms.Select(attrs={'class': 'form-control'},choices=[('', 'Select')] + list(Hospitalavail.CATEGORY_CHOICES)),
        }


class HospitalAvailSearchForm(forms.Form):
    query = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by name'}))



class HospitalRequestForm(forms.ModelForm):
    class Meta:
        model = HospitalRequest
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter Message'}),
        }


         

class HospitalRequestResponseForm(forms.ModelForm):
    class Meta:
        model = HospitalRequest
        fields = ['status', 'response_message']
        widgets = {
            'status': forms.RadioSelect(choices=HospitalRequest.REQUEST_STATUS_CHOICES),
            'response_message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Response Message....'}),
        }


class HospitalDetailForm(forms.ModelForm):
    class Meta:
        model = HospitalDetail
        fields = [
            'address', 'landmark', 'city', 'state', 
            'postal_code', 'phone_number', 'country'
        ]
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter address'}),
            'landmark': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Landmark'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter city'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter state'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter postal code'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter country'}),
        }