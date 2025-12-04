from django.urls import path
from . import views

urlpatterns = [
    path('index',view=views.index,name="index"),
    path('register',view=views.register_view,name="register")
]
