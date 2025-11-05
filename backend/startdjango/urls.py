"""
URL configuration for startdjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.tags, name='tags')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='tags')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, reverse
from django.shortcuts import HttpResponse
from book import views
from django.conf.urls.static import static
from django.conf import settings


# 视图函数一般不会写到urls.py中，放在每一个app的views.py中
def index(request):
    print(reverse("index"))
    print(reverse("book_detail_query_string"))
    # 如果是在path中传入参数，url反转需要用kwargs,后面跟参数的key值对http://127.0.0.1:8000/book/1
    print(reverse("book_str", kwargs={"book_id": 1}))
    # 如果是查询字符串传参，那么就只能用字符串拼接的方式http://127.0.0.1:8000/book?id=1
    print(reverse("book_detail_query_string") + "?id=1")
    print(reverse("movie:movie_list"))
    return HttpResponse("Hello World")


urlpatterns = [
    path("admin/", admin.site.urls),
    # urls.py中只写视图的映射，不能写具体访问的url，前面自带了http://127.0.0.1:8000/
    path("", index, name="index"),  # 访问http://127.0.0.1:8000/s才能访问到index
    # 这里访问的是http://127.0.0.1:8000/book?id=1。后面的id是参数，是视图自动带过来的，参数的值是自己输入的
    path("book", views.book_detail_query_string, name="book_detail_query_string"),
    # 注意这里的book_detail_query_string是视图函数名，不能带(),否则变成函数执行的返回值了
    # http://127.0.0.1:8000/book/1
    # 1.以后在浏览器中，如果book_id输入的是一个非整数，那么会报404错误，比如输入http://127.0.0.1:8000/book/a
    # 2.在视图函数中得到的book_id就是一个整数，如果输入http://127.0.0.1:8000/book/1，那么book_id就是整数1，而不是默认的字符串类型'1'
    path("book/<int:book_id>", views.book_detail_path),
    # path('book/<int:book_id>/<str:book_name>',views.book_detail_path)
    path("book/str/<str:book_id>", views.book_str, name="book_str"),
    path("book/slug/<str:book_id>", views.book_slug, name="book_slug"),
    path("book/uuid/<uuid:book_id>", views.book_uuid, name="book_uuid"),
    path("book/path/<path:book_id>", views.book_path, name="book_path"),
    path("movie/", include("movie.urls")),
    path("tags/", include("tags.urls")),
    path("filters/", include("filters.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
