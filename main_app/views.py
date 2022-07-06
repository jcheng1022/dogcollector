from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
from .models import Dog
from django.views.generic.edit import CreateView

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')



def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request,'dogs/index.html', {'dogs':dogs})

def dogs_details(request,dog_id):
    dog = Dog.objects.get(id=dog_id)
    return render(request, 'dogs/details.html', {'dog': dog})

class DogCreate(CreateView):
    model=Dog
    fields='__all__'