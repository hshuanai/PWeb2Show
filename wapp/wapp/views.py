from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the home page")

def about(request):
    context = {'title': 'Aoubt page.'}
    
    return render(request, 'about.html', context)
