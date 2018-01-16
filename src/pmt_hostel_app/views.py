from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser, MultiPartParser, FileUploadParser
from .models import User

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

@api_view(['GET', 'POST'])
@parser_classes((JSONParser,MultiPartParser, FileUploadParser))
def register(request):
	if request.method == "POST":
		print("POST request(Registration)")
		print(request.POST)
		print(request.data) # True
		print(request.FILES)

		del request.data["ppic"]
		print("After removal: ", request.data)
		user = User(**request.data)
		user.save()
		print(user, user.id)
		return Response({"status": 200, "message": "Registration successful"}, status=200)
	elif request.method == "GET":
		template = loader.get_template("pmt_hostel_app/register.html")
		dt = datetime.now()
		current_year = int(str(dt)[0:4])
		batches = [batch for batch in range(1968, current_year)][::-1]
		context = {"batches": batches}
		print("BATCHES, ", batches)
		return HttpResponse(template.render(context, request))

def logout(request):
	template = loader.get_template("pmt_hostel_app/logout.html")
	context = {}
	return HttpResponse(template.render(context, request))

def posts(request):
	template = loader.get_template("pmt_hostel_app/posts.html")
	context = {}
	return HttpResponse(template.render(context, request))

def profile(request):
	template = loader.get_template("pmt_hostel_app/profile.html")
	context = {}
	return HttpResponse(template.render(context, request))

def st_index(request):
	template = loader.get_template("pmt_hostel_app/st_index.html")
	context = {}
	return HttpResponse(template.render(context, request))

def success(request):
	template = loader.get_template("pmt_hostel_app/success.html")
	context = {}
	return HttpResponse(template.render(context, request))

def error(request):
	template = loader.get_template("pmt_hostel_app/error.html")
	context = {}
	return HttpResponse(template.render(context, request))

# def st_index2(request):
# 	template = loader.get_template("pmt_hostel_app/st_base.html")
# 	context = {}
# 	return HttpResponse(template.render(context, request))
