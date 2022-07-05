from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


class Dog:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

dogs = [
    Dog('Coco', 'Pomeranian', 'Sleep lover', '12'),
    Dog('Oreo', 'Rotweiler', 'Friendly dog that looks scary', '5'),
    Dog('Lucky', 'Golden Retreiver', 'Loyal dog that will follow you anywhere', '2'),
    Dog('Dog', 'Chihuahua', 'Yes his name is Dog', '6')
]

def dog_index(request):
    return render (request, 'index.html', {'dogs':dogs})