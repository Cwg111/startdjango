#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :urls.py
# @Time      :2025/11/6 9:16
# @Author    :ChenWenGang
from django.urls import path
from . import views

app_name = "book"
urlpatterns = [
    path("index", views.index, name="book_index"),
    path("add", views.add_book, name="add_book"),
    path("query", views.query_book, name="query_book"),
    path("order", views.order_view, name="order_view"),
    path("update", views.update_view, name="update_view"),
    path("delete", views.delete_view, name="delete_view"),
    path("tags", views.tags_view, name="tags_view"),
]

if __name__ == "__main__":
    run_code = 0
