from django import forms
from registration.forms import RegistrationFormUniqueEmail
from django.contrib.auth.forms import User

class ProfileForm(RegistrationFormUniqueEmail):
    fullname = forms.CharField(max_length=200,required=True,widget= forms.TextInput
                           (attrs={'class':'form-control'}))
    address = forms.CharField(max_length=300,required=True,widget= forms.TextInput
                           (attrs={'class':'form-control'}))
    phone_number = forms.IntegerField(widget= forms.TextInput
                           (attrs={'class':'form-control'}))

