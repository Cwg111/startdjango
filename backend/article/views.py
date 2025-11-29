from django.shortcuts import render, HttpResponse
from datetime import datetime
from .models import User, Article, Comment


# Create your views here.
def article_test(request):
    # user = User(username="张三", password="123456")
    # user.save()
    user = User.objects.first()
    article = Article(title="hello World", content="测试文章内容", author=user)
    article.save()
    # article = Article.objects.first()
    # exit_user = User.objects.get(username="张三")
    # new_usernames = ["李四", "王五"]
    # users = [User(username=username, password="123456") for username in new_usernames]
    # for user in users:
    #     user.save()
    # articles = [
    #     Article(title="测试文章(张三)", content="测试文章内容1", author=exit_user),
    #     Article(title="测试文章(李四)", content="测试文章内容2", author=users[0]),
    #     Article(title="测试文章(王五)", content="测试文章内容3", author=users[1]),
    # ]
    # Article.objects.bulk_create(articles)
    return HttpResponse("添加成功")


def article_test_time(request):
    Article(
        title="测试时间", content="测试时区变更", author=User.objects.first()
    ).save()
    print(Article.objects.last().pub_time)
    return render(
        request, "test.html", context={"time": Article.objects.last().pub_time}
    )


def comment_test(request):
    comment = Comment(content="顶层评论")
    comment.save()
    comment1 = Comment(content="子评论1", origin_comment=comment)
    comment1.save()
    comment1_1 = Comment(content="子评论1-1", origin_comment=comment1)
    comment1_1.save()
    return HttpResponse("添加成功")


def one_to_many(request):
    user = User.objects.first()
    articles = user.articles.all()  # 查看这第一个用户下的所有文章
    for article in articles:
        print(article.title, article.content)
    return HttpResponse("查询成功")


def query1(request):
    # # 相当于sql查询里面的=
    # article = Article.objects.filter(id__exact=1).values()
    # 类似与sql查询里面的like，但是前后面没有%，相当于精确查找，但忽略大小写
    article = Article.objects.filter(title__iexact="hello world").values()
    # 查询结果.query可以看到底层执行的sql语句，比如现在这个article.query
    print(article.query)
    print(list(article))
    return HttpResponse("查询成功")


def query2(request):
    # 模糊查询，类似于sql查询里面的like，但是前后面有%，相当于精确查找，大小写敏感,区分大小写
    # article = Article.objects.filter(title__contains="world").values()
    # 模糊查询，类似于sql查询里面的like，但是前后面有%，相当于精确查找，大小写不敏感,不区分大小写
    article = Article.objects.filter(title__icontains="world").values()
    print(article.query)
    print(list(article))
    return HttpResponse("查询成功")


def query3(request):
    article = Article.objects.filter(id__in=[1, 2, 3])
    print(article.query)
    print(list(article))
    return HttpResponse("查询成功")


def query4(request):
    start_time = datetime(2025, 11, 1)
    end_time = datetime(2025, 11, 12)
    article = Article.objects.filter(pub_time__range=(start_time, end_time))
    print(article.query)
    print(list(article))
    return HttpResponse("查询成功")


def query5(request):
    user = User.objects.filter(articles__title__contains="hello")
    print(user.query)
    print(list(user))
    return HttpResponse("查询成功")
