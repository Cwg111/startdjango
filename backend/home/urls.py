#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :urls.py
# @Time      :2025/11/4 15:13
# @Author    :ChenWenGang
from django.urls import path

from movie.urls import app_name
from . import views

urlpatterns = [
    path('', views.index, name='home_index'),
    path('baidu', views.index_baidu, name='home_baidu'),
    path('info',views.info,name='home_info')


]

if __name__ == "__main__":
    run_code = 0
