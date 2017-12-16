from django.db import models
from . import conf

class User(models.Model):
	"""
	User model that describes the structure of fields required to store basic user details
	"""
	full_name = models.CharField(max_length=conf.USER_FULL_NAME_MAX_LENGTH, null=False, blank=False)
	email = models.EmailField(max_length=conf.USER_EMAIL_MAX_LENGTH, null=True, blank=True, unique=True)
	contact = models.CharField(max_length=10, null=False, blank=False)
	dob = models.DateField(null=False, blank=False)
	password = models.CharField(max_length=20, null=False, blank=False)
	quote = models.TextField()

	def __str__(self):
		return self.full_name + "-" + self.email



