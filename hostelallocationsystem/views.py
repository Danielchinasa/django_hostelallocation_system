from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    # return HttpResponse('Hey Welcome to the HOME page')
    return render(request, 'home.html')

def about(request):
   # return HttpResponse('Hey Welcome to the About Page')
   return render(request, 'about.html')