from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
from .models import Dog

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')



def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request,'dogs/index.html', {'dogs':dogs})