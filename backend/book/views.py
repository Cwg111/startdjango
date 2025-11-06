from django.shortcuts import render, HttpResponse
from django.db import connection
from .models import BookModel, Author, Tags

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


def index(request):
    cursor = connection.cursor()
    cursor.execute("select * from book_bookmodel")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return HttpResponse("查找成功")


def add_book(request):
    book = BookModel(name="三国演义", author="罗贯中")
    author = Author(
        username="ChenWenGang", email="123", website="123", profile="我好想玩游戏"
    )
    book.save()
    author.save()
    # books = [
    #     BookModel(name="三国演义", author="罗贯中", price=99.9),
    #     BookModel(name="水浒传", author="施耐庵", price=89.9),
    #     BookModel(name="红楼梦", author="曹雪芹", price=79.9),
    #     BookModel(name="西游记", author="吴承恩", price=69.9),
    #     BookModel(name="三国演义", author="罗贯中", price=59.9),
    #     BookModel(name="水浒传", author="施耐庵", price=49.9),
    # ]
    # BookModel.objects.bulk_create(books)
    return HttpResponse("图书插入添加成功")


def query_book(request):
    # books = BookModel.objects.all()
    # books = BookModel.objects.filter(name="三国演义")
    # print(type(books))
    # print(books)
    # for book in books:
    #     print(book.id, book.name, book.pub_time, book.price)
    try:
        book = BookModel.objects.get(name="三国演义11")
        print(book.id, book.name, book.pub_time, book.price)
    except BookModel.DoesNotExist:
        print("没有找到")
    return HttpResponse("查找成功!")


def order_view(request):
    # books = BookModel.objects.order_by("-price")
    books = BookModel.objects.all()
    for book in books:
        print(book.id, book.name, book.pub_time, book.price)
    return HttpResponse("按价格从大到下排序成功!")


def update_view(request):
    BookModel.objects.filter(name="三国演义").update(name="三国")
    return HttpResponse("更新成功!")


def delete_view(request):
    BookModel.objects.filter(name="三国").delete()
    return HttpResponse("删除成功!")


def tags_view(request):
    tag = Tags()
    tag.save()
    return HttpResponse("添加成功")
