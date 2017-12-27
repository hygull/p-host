# URLconf file named urls.py

from django.urls import path
from . import views


urlpatterns = [
	path("", views.index, name="index"),
	path("contact/", views.contact, name="contact"),
	path("members/", views.members, name="members"),
	path("posts/", views.posts, name="posts"),
	path("register/", views.logout, name="logout"),
	path("login/", views.login, name="login"),
	path("logout/", views.logout, name="logout"),
	path("st_index/", views.st_index, name="st_index"),
	path("st_index2/", views.st_index, name="st_index2"),
]