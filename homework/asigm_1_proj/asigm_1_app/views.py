from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    response = HttpResponse()
    response.write("<h1> Thao Nguyen</h1>")
    response.write("This is Thao Ng's first Django application")
    return response