from django.views import generic
from apps.miningapp.models import *
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


class GPUList(generic.ListView):
    queryset = GPU.objects.all()
    template_name = 'index.html'
    #html_template = loader.get_template('index.html')


class GPUDetail(generic.DetailView):
    model = GPU
    template_name = 'gpu_details.html'
    #html_template = loader.get_template('apps/templates/miningapp/gpu_details.html')
