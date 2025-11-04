#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :urls.py
# @Time      :2025/11/4 15:13
# @Author    :ChenWenGang
from django.urls import path
from . import views

app_name = "home"
urlpatterns = [
    path("", views.index, name="home_index"),
    path("baidu", views.index_baidu, name="home_baidu"),
    path("info", views.info, name="home_info"),
    path("if", views.if_demo, name="home_if"),
    path("for", views.for_demo, name="home_for"),
    path("with", views.with_demo, name="home_with"),
    path("url", views.url_demo, name="home_url"),
    path("book/<int:book_id>", views.book_demo, name="home_book"),
    path("book", views.book_demo_query_string, name="home_book_query_string"),
    path(
        "book/<int:user_id>/<str:user_name>", views.book_demo_mix, name="home_book_mix"
    ),
]

if __name__ == "__main__":
    run_code = 0
