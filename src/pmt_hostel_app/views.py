from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def demo(request):
    return HttpResponse("<center><h1>Hello PMT Hostelers</h1></center>")

def index(request):
	template = loader.get_template("pmt_hostel_app/index.html")
	context = {
		"name": "Rishikesh Agrawani"
	}
	return HttpResponse(template.render(context, request))