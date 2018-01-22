# URLconf file named urls.py

from django.urls import path, re_path, include
from . import views


urlpatterns = [
	# path("", views.index, name="index"),
	path("contact/", views.contact, name="contact"),
	path("members/", views.members, name="members"),
	path("pmt-member/<int:id>/", views.pmt_member, name="pmt-member"),
	path("api/pmt-member/<str:email>/", views.pmt_member_user, name="pmt-member-user"),
	path("posts/", views.posts, name="posts"),
	path("register/", views.register, name="logout"),
	path("profile/", views.profile, name="profile"),
	path("profile/edit/<str:email>/", views.profile_edit, name="profile_edit"),
	path("login/", views.login, name="login"),
	path("logout/", views.logout, name="logout"),
	path("", views.st_index, name="st_index"),
	path("st_index2/", views.st_index, name="st_index2"),
	path("success/", views.success, name="success"),
	path("error/", views.error, name="error"),
	path("forgot-password/", views.forgot_password, name="forgot-password"),
	path("email-confirmation/chfcRjhdIqiyeSdg64HffjI234K74sdoasyxoyuwbahntdhdhduecdggEkjhhgsre43ShwytdHkaAhdgGporrRnsfdfAqWktrNhygullI/<int:pk>/<str:email_md5>/<str:email>/",
		views.email_confirmation, name="email-confirmation"
	),
	path("api/send-confirmation-email/", views.send_confirmation_email, name="send-confirmation-email"),

	re_path(r'^api-auth/', include('rest_framework.urls')),
]