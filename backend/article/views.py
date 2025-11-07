from django.shortcuts import render, HttpResponse
from .models import User, Article, Comment


# Create your views here.
def article_test(request):
    # user = User(username="张三", password="123456")
    # user.save()
    # article = Article(title="测试文章", content="测试文章内容", author=user)
    # article.save()
    # article = Article.objects.first()
    exit_user = User.objects.get(username="张三")
    new_usernames = ["李四", "王五"]
    users = [User(username=username, password="123456") for username in new_usernames]
    for user in users:
        user.save()
    articles = [
        Article(title="测试文章(张三)", content="测试文章内容1", author=exit_user),
        Article(title="测试文章(李四)", content="测试文章内容2", author=users[0]),
        Article(title="测试文章(王五)", content="测试文章内容3", author=users[1]),
    ]
    Article.objects.bulk_create(articles)
    return HttpResponse("添加成功")


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
