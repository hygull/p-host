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