from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def demo(request):
    return HttpResponse("<center><h1>Hello PMT Hostelers</h1></center>")

def index(request):
	template = loader.get_template("pmt_hostel_app/index.html")
	context = {}
	return HttpResponse(template.render(context, request))

def members(request):
	template = loader.get_template("pmt_hostel_app/members.html")
	context = {}
	return HttpResponse(template.render(context, request))

def contact(request):
	template = loader.get_template("pmt_hostel_app/contact.html")
	context = {}
	return HttpResponse(template.render(context, request))

def login(request):
	template = loader.get_template("pmt_hostel_app/login.html")
	context = {}
	return HttpResponse(template.render(context, request))

def register(request):
	template = loader.get_template("pmt_hostel_app/register.html")
	context = {}
	return HttpResponse(template.render(context, request))

def logout(request):
	template = loader.get_template("pmt_hostel_app/logout.html")
	context = {}
	return HttpResponse(template.render(context, request))

def posts(request):
	template = loader.get_template("pmt_hostel_app/posts.html")
	context = {}
	return HttpResponse(template.render(context, request))

def st_index(request):
	template = loader.get_template("pmt_hostel_app/st_index.html")
	context = {}
	return HttpResponse(template.render(context, request))

# def st_index2(request):
# 	template = loader.get_template("pmt_hostel_app/st_base.html")
# 	context = {}
# 	return HttpResponse(template.render(context, request))
