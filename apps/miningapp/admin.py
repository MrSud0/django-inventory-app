from django.contrib import admin
from apps.miningapp.models import Hashrate,Motherboard,Coin, GPU
from django.views import generic
from apps.miningapp.models import *
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

# Register your models here.
admin.site.register(Hashrate)
admin.site.register(Motherboard)
admin.site.register(Coin)


class GPUAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'price', 'wattage')
    list_filter = ("price",)
    search_fields = ['name','memory','wattage']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(GPU, GPUAdmin)
