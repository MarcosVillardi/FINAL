from django.shortcuts import render
from . import forms
from . import models
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class Reserva_list(ListView):
    model = models.Reserva
    template_name = 'blog/reserva_list.html'
    context_object_name = 'reservas'

class Reserva_create(CreateView):
    model = models.Reserva
    template_name = 'blog/reserva_create.html'
    form_class = forms.ReservaForm
    success_url = reverse_lazy('home:index')

class Reserva_delete(DeleteView):
    model = models.Reserva
    template_name = 'blog/reserva_delete.html'
    success_url = reverse_lazy('home:index')

class Reserva_update(UpdateView):
    model = models.Reserva
    template_name = 'blog/reserva_update.html'
    form_class = forms.ReservaForm
    success_url = reverse_lazy('home:index')

def reserva_index(request):
    return render(request, 'blog/reserva_index.html')

class Garaje_list(ListView):
    model = models.Garaje
    template_name = 'blog/garaje_list.html'
    context_object_name = 'garajes'

class Garaje_create(CreateView):
    model = models.Garaje
    template_name = 'blog/garaje_create.html'
    form_class = forms.GarajeForm
    success_url = reverse_lazy('home:index')

class Garaje_delete(DeleteView):
    model = models.Garaje
    template_name = 'blog/garaje_delete.html'
    success_url = reverse_lazy('home:index')

class Garaje_update(UpdateView):
    model = models.Garaje
    template_name = 'blog/garaje_update.html'
    form_class = forms.GarajeForm
    success_url = reverse_lazy('home:index')

def garaje_index(request):
    return render(request, 'blog/garaje_index.html')