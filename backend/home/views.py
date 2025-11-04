from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html")


def index_baidu(request):
    return render(request, "baidu.html")


def info(request):
    # 普通类型
    username = "小明"
    #  字典类型
    book = {"name": "python", "price": 100}
    # 列表类型
    books = [
        {"name": "水浒传", "author": "施耐庵"},
        {"name": "三国演义", "author": "罗贯中"},
    ]

    # 对象
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    context = {
        "username": username,
        "book": book,
        "books": books,
        "person": Person("小王", 18),
    }
    return render(request, "info.html", context=context)
