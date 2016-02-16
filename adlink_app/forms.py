from adlink_app import admin
from django.contrib.auth.models import User
from django import forms
from .models import admin
from uni_form.helper import FormHelper
from crispy_forms.helper import FormHelper

class authentication(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password',)
class additionalforms(forms.ModelForm):
	
	class Meta:
		model = admin
		fields = ('firstname', 'lastname', 'company','profile_pic',)
			
		