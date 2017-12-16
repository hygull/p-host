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