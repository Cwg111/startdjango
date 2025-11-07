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
    path("comment_test", views.comment_test, name="comment_test"),
    path("one_to_many", views.one_to_many, name="one_to_many"),
]
if __name__ == "__main__":
    run_code = 0
