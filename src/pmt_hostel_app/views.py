from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import redirect
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser, MultiPartParser, FileUploadParser
from .models import User
from django.core.mail import send_mail
import _thread
import hashlib


def send_email(subject, message, html_message, sender, recipients):
	send_mail(
	    subject,
	    message,
	    sender,
	    recipients,
	    fail_silently=True,
	    html_message = html_message
	)
	print("Email thread is exiting")

def get_url(email):
	email_md5 = hashlib.md5(email.encode('utf-8')).hexdigest()
	print("EMAIL MD5 ", email, email_md5)
	return email_md5

def demo(request):
    return HttpResponse("<center><h1>Hello PMT Hostelers</h1></center>")

def index(request):
	template = loader.get_template("pmt_hostel_app/index.html")
	context = {}
	return HttpResponse(template.render(context, request))

def members(request):
	template = loader.get_template("pmt_hostel_app/members.html")
	users = User.objects.all()
	context = {"users": users, "total_users": len(users)}
	return HttpResponse(template.render(context, request))

def pmt_member(request, id):
	try:
		print(id, type(id))
		template = loader.get_template("pmt_hostel_app/pmtmember.html")
		user = User.objects.get(id=int(id))
		context = {"user": user}
		return HttpResponse(template.render(context, request))
	except User.DoesNotExist:
		return redirect("/error/")

@api_view(["POST"])
def pmt_member_user(request, email):
	user = {}
	try:
		print(id, type(id))
		user_q = User.objects.get(email=email)
		user["fullname"] = user_q.fullname
		user["email"] = user_q.email 
		user["contact"] = user_q.contact
		user["batch"] = user_q.batch
		user["quote"] = user_q.batch 

		return Response({"user" : user, "status": 200}, status=200)
	except User.DoesNotExist:
		return Response({"message": "User does not exist", "status": 400}, status=200)

@api_view(["POST"])
def pmt_member_user(request, email):
	user = {}
	try:
		print(id, type(id))
		user_q = User.objects.get(email=email)
		user["fullname"] = user_q.fullname
		user["email"] = user_q.email 
		user["contact"] = user_q.contact
		user["batch"] = user_q.batch
		user["quote"] = user_q.quote

		return Response({"user" : user, "status": 200}, status=200)
	except User.DoesNotExist:
		return Response({"message": "User does not exist", "status": 400}, status=200)


def profile_edit(request, email):
	try:
		template = loader.get_template("pmt_hostel_app/edit_profile.html")
		print(id, type(id))
		user  = User.objects.get(email=email)
		dt = datetime.now()
		current_year = int(str(dt)[0:4])
		batches = [batch for batch in range(1968, current_year)][::-1]
		context = {"batches": batches, "user" : user}
		return HttpResponse(template.render(context, request))
	except User.DoesNotExist:
		return redirect("/error/")

def contact(request):
	template = loader.get_template("pmt_hostel_app/contact.html")
	context = {}
	return HttpResponse(template.render(context, request))

@api_view(['GET', 'POST'])
def login(request):
	if request.method == "GET":
		template = loader.get_template("pmt_hostel_app/login.html")
		context = {}
		return HttpResponse(template.render(context, request))
	elif request.method == 'POST':
		print("LOGIN DATA: ", request.data)
		try:
			user = User.objects.get(**request.data)
			print("GOT user as ", user.fullname)
			return Response({"message": "Successfully logged in", "status": 200, "usedId": user.pk, "email": user.email}, status=200)
		except User.DoesNotExist:
			print("Could not found user")
			return Response({"message": "User does not exist", "status": 400}, status=400)

@api_view(['GET', 'POST', 'PUT'])
@parser_classes((JSONParser,MultiPartParser, FileUploadParser))
def register(request):
	print("REQUEST METHOD", request.method)
	try:
		if request.method == "POST":
			print("POST request(Registration)")
			# print(request.POST)
			print("REGISTER DATA: ", request.data) # True
			# print(request.FILES)

			# del request.data["ppic"]
			print("After removal: ", request.data)
			user = None
			rough_text = "chfcRjhdIqiyeSdg64HffjI234K74sdoasyxoyuwbahntdhdhduecdggEkjhhgsre43ShwytdHkaAhdgGporrRnsfdfAqWktrNhygullI"
			try:
				user = User.objects.get(email=request.data["email"])
				if user.account_confirmed:
					print("User email found in DB and confirmed")
					return Response({"status": 400, "message": "This email is already registered"}, status=400)
				else:
					print("User email found in DB and not confirmed")
					print("Firing email sender thread")
					data_email_tup = (
						"PMT ACCOUNT RE-CONFIRMATION",
						"",
						"<p>Dear <b>" + user.fullname + "</b>,<br>" +
						"Click <a href='http://127.0.0.1:8000/email-confirmation/" + rough_text + "/"  + str(user.pk) + "/" + get_url(user.email) + "/" + user.email + "/'>here</a> to confirm/activate your PMT account.",
						"rishikesh0014051992@gmail.com",
						[user.email] 
					)
					_thread.start_new_thread(send_email, data_email_tup)
					print("Email thread exited")
					return Response({"status": 400, "message": "This email is already registered but not confirmed, please check your mail again"}, status=400)
			except User.DoesNotExist:
				user = User(**request.data)
				user.save()
				print(user, user.id)
				print("Firing email sender thread")
				data_email_tup = (
						"PMT ACCOUNT CONFIRMATION",
						"",
						"<p>Dear <b>" + user.fullname + "</b>,<br>" \
						"Click <a href='http://127.0.0.1:8000/email-confirmation/" + rough_text + "/" + str(user.pk) + "/" + get_url(user.email) + "/" + user.email + "/'>here</a> to confirm/activate your PMT account.",
						"rishikesh0014051992@gmail.com",
						[user.email] 
				)
				_thread.start_new_thread(send_email, data_email_tup)
				print("Email thread exited")
				return Response({"status": 200, "message": "Registration successful"}, status=200)
		elif request.method == "PUT":
			try:
				print ("PROFILE UPDATE REQUEST", request.data)
				user = User.objects.filter(email=request.data["emailLocalStoraged"])
				print(user)
				del request.data["emailLocalStoraged"]
				user.update(**request.data)
				print("Data successfully updated")
				return Response({"status": 200, "message": "Your profile has been successfully updated"}, status=200)
			except User.DoesNotExist:
				return Response({"status": 400, "message": "User does not exist"}, status=200)
			except Exception as e:
				print(e)
				return Response({"status": 500, "message": "Internal server error"}, status=200)
		elif request.method == "GET":
			template = loader.get_template("pmt_hostel_app/register.html")
			dt = datetime.now()
			current_year = int(str(dt)[0:4])
			batches = [batch for batch in range(1968, current_year)][::-1]
			context = {"batches": batches}
			print("BATCHES, ", batches)
			return HttpResponse(template.render(context, request))
	except Exception as e:
		print (e)
		return Response({"status": 400, "message": "Server side error"}, status=400)

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


def email_confirmation(request, pk, email, email_md5):
	print (email, email_md5)
	if get_url(email) == email_md5:
		try:
			user = User.objects.get(email=email, pk=pk)
			user.account_confirmed = True
			user.save()
			print("User with email " + user.email + " confirmed the account")
			template = loader.get_template("pmt_hostel_app/account-confirmed.html")
			context = {}
			return HttpResponse(template.render(context, request))
		except User.DoesNotExist:
			print("This id, email cannot be confirmed")
			return redirect("/error/")
		except:
			return redirect("/error/")
	else:
		print ("Email and its encoded value does not match")
		return redirect("/error/")
