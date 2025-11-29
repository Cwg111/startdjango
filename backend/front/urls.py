# -*- coding: utf -8 -*- #
"""
@filename:urls.py
@author:ChenWenGang
@time:2025-11-29
"""
from django.urls import path
from urllib3.util import ssl_wrap_socket

from . import views

urlpatterns = [
    path("avg", view=views.avg_view, name="avg"),
    path("count", views.count_view, name="count_view"),
    path("max_min",view=views.max_min_view,name="max_min"),
    path("sum",view=views.sum_view,name="sum"),
    path("f",view=views.f_view,name="f"),
    path("q",view=views.q_view,name="q"),
]

if __name__ == "__main__":
    pass
