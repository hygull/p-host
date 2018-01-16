# URLconf file named urls.py

from django.urls import path, re_path, include
from . import views


urlpatterns = [
	# path("", views.index, name="index"),
	path("contact/", views.contact, name="contact"),
	path("members/", views.members, name="members"),
	path("posts/", views.posts, name="posts"),
	path("register/", views.register, name="logout"),
	path("profile/", views.profile, name="profile"),
	path("login/", views.login, name="login"),
	path("logout/", views.logout, name="logout"),
	path("", views.st_index, name="st_index"),
	path("st_index2/", views.st_index, name="st_index2"),
	path("success/", views.success, name="success"),
	path("error/", views.error, name="error"),

	re_path(r'^api-auth/', include('rest_framework.urls')),
]