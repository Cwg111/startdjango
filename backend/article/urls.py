#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :urls.py
# @Time      :2025/11/7 9:31
# @Author    :ChenWenGang

from django.urls import path
from . import views

app_name = "article"
urlpatterns = [
    path("test", views.article_test, name="article_test"),
    path("test_time", views.article_test_time, name="article_test_time"),
    path("comment_test", views.comment_test, name="comment_test"),
    path("one_to_many", views.one_to_many, name="one_to_many"),
    path("query1", views.query1, name="query1"),
    path("query2", views.query2, name="query2"),
    path("query3", views.query3, name="query3"),
    path("query4", views.query4, name="query4"),
    path("query5", views.query5, name="query5"),
]
if __name__ == "__main__":
    run_code = 0
