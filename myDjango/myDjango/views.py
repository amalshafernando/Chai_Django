
from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    return render(request, 'websites/homepage.html')


def about(request):
    return render (request, 'websites/about.html')


def contact(request):
    return render (request, 'websites/contact.html')

