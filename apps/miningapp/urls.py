# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.miningapp import views

urlpatterns = [

    path('', views.GPUList.as_view(), name = 'home'),
    path('<slug:slug>/', views.GPUDetail.as_view(), name = 'gpu_detail'),

]
