from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def About(request):
    return HttpResponse("<h1>this is the about section</h1>")