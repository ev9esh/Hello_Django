#from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return render(request, 'about.html', {'greeting': 'hello'})


def home(request):
    return render(request, 'home.html', )
