from django.shortcuts import render, redirect

from django.http import HttpResponse
# Create your views here.
from .models import Dog, Toy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic import DetailView
from .forms import PlayedForm

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')



def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request,'dogs/index.html', {'dogs':dogs})

def dogs_details(request,dog_id):
    dog = Dog.objects.get(id=dog_id)
    played_form = PlayedForm()
    toys_dog_doesnt_have = Toy.objects.exclude(id__in = dog.toys.all().values_list('id'))
    played_form = PlayedForm()
    return render(request, 'dogs/details.html', {'dog': dog, 'played_form':played_form, 'toys':toys_dog_doesnt_have})

class DogCreate(CreateView):
    model=Dog
    fields='__all__'

class DogUpdate(UpdateView):
    model=Dog
    fields=['breed','description', 'age']

class DogDelete(DeleteView):
    model=Dog
    success_url= '/dogs/'


def add_playing(request, dog_id):
    form = PlayedForm(request.POST)
    if form.is_valid():
        new_playing = form.save(commit=False)
        new_playing.dog_id = dog_id
        new_playing.save()
    return redirect('detail', dog_id=dog_id)


def assoc_toy(request, dog_id, toy_id):
    Dog.objects.get(id=dog_id).toys.add(toy_id)
    return redirect('detail', dog_id = dog_id)


class ToyList(ListView):
    model = Toy
    template_name = 'toys/index.html'


class ToyDetail(DetailView):
    model = Toy
    template_name = 'toys/detail.html'