#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :urls.py
# @Time      :2025/11/5 10:15
# @Author    :ChenWenGang
from django.urls import path
from . import views

app_name = "filters"
urlpatterns = [
    path("", views.index, name="filters_index"),
    path("demo", views.filters_demo, name="filters_demo"),
    path("template/form", views.template_form, name="template_form"),
    path("static_url", views.static_view, name="static_view"),
]

if __name__ == "__main__":
    run_code = 0
