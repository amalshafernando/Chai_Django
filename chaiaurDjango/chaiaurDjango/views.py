from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello world - home page")

def about(request):
    return HttpResponse("Hello world - about page")
