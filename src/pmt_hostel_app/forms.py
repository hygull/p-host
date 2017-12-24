from django import forms
from .models import User
from django.contrib.auth.models import User, Group

class UserForm(forms.ModelForm):
	group = forms.MultipleChoiceField(queryset=Group.objects.all())

	class Meta:
		model = User
