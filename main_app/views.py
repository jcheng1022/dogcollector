from django.shortcuts import render, redirect

from django.http import HttpResponse
# Create your views here.
from .models import Dog, Toy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic import DetailView
from .forms import PlayedForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


@login_required
def dogs_index(request):
    dogs = Dog.objects.filter(user=request.user)
    return render(request,'dogs/index.html', {'dogs':dogs})
@login_required
def dogs_details(request,dog_id):
    dog = Dog.objects.get(id=dog_id)
    played_form = PlayedForm()
    toys_dog_doesnt_have = Toy.objects.exclude(id__in = dog.toys.all().values_list('id'))
    played_form = PlayedForm()
    return render(request, 'dogs/details.html', {'dog': dog, 'played_form':played_form, 'toys':toys_dog_doesnt_have})

class DogCreate(LoginRequiredMixin, CreateView):
    model=Dog
    fields=['name', 'breed', 'description', 'age']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DogUpdate(LoginRequiredMixin, UpdateView):
    model=Dog
    fields=['breed','description', 'age']

class DogDelete(LoginRequiredMixin, DeleteView):
    model=Dog


@login_required
def add_playing(request, dog_id):
    form = PlayedForm(request.POST)
    if form.is_valid():
        new_playing = form.save(commit=False)
        new_playing.dog_id = dog_id
        new_playing.save()
    return redirect('detail', dog_id=dog_id)

@login_required
def assoc_toy(request, dog_id, toy_id):
    Dog.objects.get(id=dog_id).toys.add(toy_id)
    return redirect('detail', dog_id = dog_id)
@login_required
def assoc_toy_del(request, dog_id, toy_id):
    Dog.objects.get(id=dog_id).toys.remove(toy_id)
    return redirect('detail', dog_id = dog_id)


class ToyList(LoginRequiredMixin, ListView):
    model = Toy
    template_name = 'toys/index.html'


class ToyDetail(LoginRequiredMixin, DetailView):
    model = Toy
    template_name = 'toys/detail.html'

class ToyCreate(LoginRequiredMixin, CreateView):
    model = Toy
    fields= ['name','color']

class ToyUpdate(LoginRequiredMixin, UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
    model = Toy
    success_url = '/toys/'


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)