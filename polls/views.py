from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hi there you are in polls app constituency")
    


