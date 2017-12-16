# Django docs for Django 2.0

[Download DJANGO pdf here](https://media.readthedocs.org/pdf/django/2.0.x/django.pdf)

1. [Django documentation](https://docs.djangoproject.com/en/2.0/intro/tutorial01/)

2. [Writing your first Django app, Part 1](https://docs.djangoproject.com/en/2.0/intro/tutorial01/)

3. [Quick install guide](https://docs.djangoproject.com/en/2.0/intro/install/)

```
>>> import django
>>> print(django.get_version())
2.0
```

4. [Writing your first Django app, part 2](https://docs.djangoproject.com/en/2.0/intro/tutorial02/)

Creating Admin User, Migration, Playing with the API

```
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

5. [Writing your first Django app, part 3](https://docs.djangoproject.com/en/2.0/intro/tutorial03/)

Writing more views, Raising a 404 error, Removing hardcoded URLs in templates, Namespacing URL names

6. [Writing your first Django app, part 4](https://docs.djangoproject.com/en/2.0/intro/tutorial04/)

Write a simple form, Generic views

7. [Writing your first Django app, part 5]( https://docs.djangoproject.com/en/2.0/intro/tutorial05/ )

Wrinting Tests

8. [Writing your first Django app, part 6](https://docs.djangoproject.com/en/2.0/intro/tutorial06/)

Using CSS

9. [Writing your first Django app, part 7](https://docs.djangoproject.com/en/2.0/intro/tutorial07/)

Customize the admin form, Customizing your project’s templates, Customizing Django admin interface

Create a templates directory in your project directory (the one that contains manage.py). Templates can live anywhere on your filesystem that Django can access. (Django runs as whatever user your server runs.) However, keeping your templates within the project is a good convention to follow.

Open your settings file (mysite/settings.py, remember) and add a DIRS option in the TEMPLATES setting

Read [Reusable apps](https://docs.djangoproject.com/en/2.0/intro/reusable-apps/) to know about **Packaging your apps**


**Note:** Read all notes from this page

```
mysite/settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

10. [django-admin and manage.py](https://docs.djangoproject.com/en/2.0/ref/django-admin/)

11. [Packages](https://docs.python.org/3/tutorial/modules.html#tut-packages)

12. [Django settings](https://docs.djangoproject.com/en/2.0/topics/settings/)

13. [URL dispatcher](https://docs.djangoproject.com/en/2.0/topics/http/urls/)


