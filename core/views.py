from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("LifeLink – Emergency Blood & Organ Management System")

# Create your views here.
