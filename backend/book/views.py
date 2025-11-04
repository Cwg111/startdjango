from django.shortcuts import render, HttpResponse


# Create your views here.
# 在url中携带参数
# 1.通过查询字符串（query string）:https://www.baidu.com/s?wd=python&a=1&b=2
# 2.在path中携带：https://www.baidu.com/s/python/1

# 通过查询字符串获取参数
def book_detail_query_string(request):
    # 获取参数 request.GET={"id":3} 相当于一个字典根据key值取value
    book_id = request.GET.get("id")  # 推荐使用get('id'),
    # get()方法如果没找到key为id的键值对会返回None，当使用[]方式获取时，如果没找到会报错
    name = request.GET.get("name")
    return HttpResponse(f"图书id是：{book_id}，图书名称是：{name}")


# 在path中携带参数
def book_detail_path(request, book_id):
    return HttpResponse(f"图书id是：{book_id}")


# def book_detail_path(request, book_id,book_name):
#     return HttpResponse(f"图书id是：{book_id}，图书名称是：{book_name}")

def book_str(request, book_id):
    return HttpResponse(f"图书id是：{book_id}")


def book_slug(request, book_id):
    return HttpResponse(f"图书id是：{book_id}")


def book_uuid(request, book_id):
    return HttpResponse(f"图书id是：{book_id}")

def book_path(request, book_id):
    return HttpResponse(f"图书id是：{book_id}")
