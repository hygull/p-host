### 1

[Writing your first Django app, part 3](https://docs.djangoproject.com/en/2.0/intro/tutorial03/)

A view is a “type” of Web page in your Django application that generally serves a 
specific function and has a specific template. 


1. class based views

2. function based views

In Django, web pages and other content are delivered by views. Each view is represented by a 
simple Python function (or method, in the case of class-based views). 

Django will choose a view by examining the URL that’s requested (to be precise, the part of 
the URL after the domain name).


### 2

Write views that actually do something¶
Each view is responsible for doing one of two things: returning an HttpResponse object containing the content for the requested page, or raising an exception such as Http404. The rest is up to you.

Your view can read records from a database, or not. It can use a template system such as Django’s – or a third-party Python template system – or not. It can generate a PDF file, output XML, create a ZIP file on the fly, anything you want, using whatever Python libraries you want.

All Django wants is that HttpResponse. Or an exception.


### 3

```
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```

A shortcut: render()
It’s a very common idiom to load a template, fill a context and return an HttpResponse object with the result of the rendered template. Django provides a shortcut. Here’s the full index() view, rewritten:

polls/views.py

```
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

```