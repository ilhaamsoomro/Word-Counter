from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def display(request):
    return render(request, 'index.html')

def shower(request):
    return render(request, 'index2.html')