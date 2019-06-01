from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):

    date_tracker = "Date Tracker Application"
    return HttpResponse(date_tracker)