from django.shortcuts import render

# Create your views here.
def all_chai(request):
    return render(request, 'chai/all_chai.html')

def menu(request):
    return render(request, 'chai/menu.html')


