from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

def index(request):
    return render(request, 'index.html')

def project(request):
    return render(request, 'project.html')