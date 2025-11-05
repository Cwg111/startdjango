#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :urls.py
# @Time      :2025/11/4 15:13
# @Author    :ChenWenGang
from django.urls import path
from . import views

app_name = "tags"
urlpatterns = [
    path("", views.index, name="tags_index"),
    path("baidu", views.index_baidu, name="tags_baidu"),
    path("info", views.info, name="tags_info"),
    path("if", views.if_demo, name="tags_if"),
    path("for", views.for_demo, name="tags_for"),
    path("with", views.with_demo, name="tags_with"),
    path("url", views.url_demo, name="tags_url"),
    path("book/<int:book_id>", views.book_demo, name="tags_book"),
    path("book", views.book_demo_query_string, name="tags_book_query_string"),
    path(
        "book/<int:user_id>/<str:user_name>", views.book_demo_mix, name="tags_book_mix"
    ),
    path("spaceless", views.spaceless_demo, name="tags_spaceless"),
    path("autoescape", views.autoescape_demo, name="tags_autoescape"),
]

if __name__ == "__main__":
    run_code = 0
