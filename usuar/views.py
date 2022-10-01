from multiprocessing.sharedctypes import Value
from unicodedata import name
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView,ListView
from usuar.forms import *
from usuar.models import *

# Create your views here.

class Postulante(CreateView):
    model = Postulante
    template_name = "form.html"
    success_url = reverse_lazy('Trabajaconnosotros/')
    form_class = PostulanteForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'TRABAJA CON NOSOTROS'
        context['action'] = 'add'
        return context


class Inicio(ListView):
    template_name = "inicio.html"
    model = Empresa
    context_object_name = 'detalle'
    success_url = reverse_lazy('Inicio')
    #queryset = Cliente.objects.filter(estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Inicio'
        context['url_anterior'] = 'Trabajaconnosotros/'
        context['query'] = self.request.GET.get("query") or ""
        return context

class Quienessomos(TemplateView):
    template_name = 'quienessomos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "quienessomos"
        return context