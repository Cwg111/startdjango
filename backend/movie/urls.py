#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :urls.py
# @Time      :2025/11/4 10:11
# @Author    :ChenWenGang
from django.urls import path
from . import views
#指定应用名称（应用命名空间）
app_name='movie'
urlpatterns=[
    path('list',views.movie_list,name='movie_list'),
    path('detail/<int:movie_id>',views.movie_detail,name='movie_detail')
]

if __name__ == "__main__":
    run_code = 0
