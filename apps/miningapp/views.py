from django.views import generic
from .models import *
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


class GPUList(generic.ListView):
    queryset = GPU.objects.order_by('price')
    template_name = 'index.html'
    html_template = loader.get_template('miningapp/index.html')

class GPUDetail(generic.DetailView):
    model = GPU
    template_name = 'gpu_detail.html'
