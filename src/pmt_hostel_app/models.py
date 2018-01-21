from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from . import conf


class User(models.Model):
	"""
	User model that describes the structure of fields required to store basic user details
	"""
	fullname = models.CharField(max_length=conf.USER_FULL_NAME_MAX_LENGTH, null=False, blank=False, help_text=_("Enter your full name"))
	email = models.EmailField(max_length=conf.USER_EMAIL_MAX_LENGTH, null=False, blank=False, unique=True, help_text=_("Enter your email, eg. rishikesh0014051992@gmail.com"))
	contact = models.CharField(max_length=10, null=False, blank=False, help_text=_("Enter your 10 digit mobile number"))
	dob = models.DateField(null=True, blank=True, help_text=_("Enter your date of birth"))
	password = models.CharField(max_length=20, null=False, blank=False, help_text=_("Enter your password"))
	quote = models.TextField(blank=True, null=True, help_text=_("Enter your popular quote, eg. Never give up and try to achieve your goal with passion"))
	batch = models.IntegerField(default=conf.USER_BATCH_CURRENT_YEAR, validators=[MinValueValidator(conf.USER_BATCH_MIN_YEAR) , MaxValueValidator(conf.USER_BATCH_CURRENT_YEAR)], 
			help_text=_("From which batch(admission year) you are, eg. " + str(conf.USER_BATCH_CURRENT_YEAR) + ", 2015, 2011 etc."))
	is_admin = models.BooleanField(default=False, help_text=_("Hi Admin, do you really want to make this person as an admin?"))
	is_active = models.BooleanField(default=False, help_text=_("Hi Admin, do you really want to make this person a PMT member?"))
	account_confirmed = models.BooleanField(default=False, help_text=_("User has confirmed his account or not"))
	ppic = models.CharField(max_length=1000, default="", blank=True, help_text=_("Name of pic inside media root"))
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False, help_text=_("The time when user registered"))
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, help_text=_("Last time when he updated the details"))

	def __str__(self):
		display_text = str(self.id) + " - " + self.fullname + ", " + self.email

		if self.account_confirmed:
			display_text += ", account has been confirmed (YES)"
		else:
			display_text += ", account has not been confirmed (NO)"

		return display_text
