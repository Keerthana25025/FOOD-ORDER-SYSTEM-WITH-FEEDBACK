from django import forms
from django.forms import ModelForm
from CrudApp.models import Registers
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from CrudApp.models import Profile

class Reg(forms.ModelForm):
	class Meta:
		model=Registers
		fields=['name','mobile','age','gender','branch']
		widgets={
		'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}),
		'mobile':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your mobile number'}),
		'age':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter your age'}),
		'gender':forms.RadioSelect(attrs={'type':'radio','placeholder':'Select your gender'}),
		'branch':forms.Select(attrs={'class':'form-control'}),
		}


class RegistrationForm(UserCreationForm):
	class Meta:
		model=User
		fields=['first_name','last_name','username','email']
		widgets={
		'first_name':forms.TextInput(attrs={'class':'form-control'}),
		'last_name':forms.TextInput(attrs={'class':'form-control'}),
		'username':forms.TextInput(attrs={'class':'form-control'}),
		'email':forms.EmailInput(attrs={'class':'form-control'}),
		}

class ProfileForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields='__all__'
		widgets={
		'name':forms.TextInput(attrs={'class':'form-control'}),
		'image':forms.ClearableFileInput(attrs={'class':'custom-image-input'}),
		}