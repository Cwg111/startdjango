from django.shortcuts import render, HttpResponse


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


def if_demo(request):
    age = 20
    return render(request, "if.html", context={"age": age})


def for_demo(request):
    # 列表
    books = [
        {"name": "水浒传", "author": "施耐庵"},
        {"name": "三国演义", "author": "罗贯中"},
    ]
    # 字典
    person = {"name": "小王", "age": 18, "height": 180}
    # 空的列表，空循环
    empty_list = []
    context = {"books": books, "person": person, "empty_list": empty_list}
    return render(request, "for.html", context=context)


def with_demo(request):
    return render(
        request,
        "with.html",
        context={"person": {"name": "小王", "age": 18, "height": 180}},
    )


def url_demo(request):
    return render(request, "url.html", context={})


#  path带参数的url
def book_demo(request, book_id):
    return HttpResponse(f"图书详情id为：{book_id}")


#  query string带参数的url
def book_demo_query_string(request):
    book_id = request.GET.get("id")
    book_name = request.GET.get("name")
    return HttpResponse(f"图书id为：{book_id},图书名称为：{book_name}")


# 多path带参数和 query string带参数的混合的 url
def book_demo_mix(request, user_id, user_name):
    book_id = request.GET.get("id")
    book_name = request.GET.get("name")
    return HttpResponse(
        f"用户id为：{user_id},用户名称为：{user_name},图书id为：{book_id},图书名称为：{book_name}"
    )
