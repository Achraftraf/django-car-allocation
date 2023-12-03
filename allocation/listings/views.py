from django.shortcuts import render
from django.http import HttpResponse

# A basic view function
def index(request):
    # Some example data
    return HttpResponse('TEST')
