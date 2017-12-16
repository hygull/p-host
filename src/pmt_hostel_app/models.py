from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from . import conf

class PmtStudent(models.Model):
	"""
	User model that describes the structure of fields required to store basic user details
	"""
	full_name = models.CharField(max_length=conf.USER_FULL_NAME_MAX_LENGTH, null=False, blank=False)
	email = models.EmailField(max_length=conf.USER_EMAIL_MAX_LENGTH, null=False, blank=False, unique=True)
	contact = models.CharField(max_length=10, null=False, blank=False)
	dob = models.DateField(null=False, blank=False)
	password = models.CharField(max_length=20, null=False, blank=False)
	quote = models.TextField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
	batch = models.IntegerField(default=conf.USER_BATCH_CURRENT_YEAR, validators=[MinValueValidator(conf.USER_BATCH_MIN_YEAR) , MaxValueValidator(conf.USER_BATCH_CURRENT_YEAR)])
	is_admin = models.BooleanField(default=False)
	account_confirmed = models.BooleanField(default=False)

	def __str__(self):
		return str(self.id) + " - " + self.full_name + ", " + self.email
