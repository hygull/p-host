from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("<center><h1>Hello PMT Hostelers</h1></center>")

