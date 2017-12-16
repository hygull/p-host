```
(venv) MacBook-Pro-2:pmt_hostel_site admin$ python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying sessions.0001_initial... OK
(venv) MacBook-Pro-2:pmt_hostel_site admin$ python3 manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
December 16, 2017 - 14:26:45
Django version 2.0, using settings 'pmt_hostel_site.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Create model named User 

```
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from . import conf

class User(models.Model):
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

```

then do the following

```
(venv) MacBook-Pro-2:src admin$ python3 manage.py makemigrations pmt_hostel_app
Migrations for 'pmt_hostel_app':
  pmt_hostel_app/migrations/0001_initial.py
    - Create model User
(venv) MacBook-Pro-2:src admin$ 
```