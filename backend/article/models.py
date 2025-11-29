import datetime

from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=100, null=False)


class UserExtension(models.Model):
    birthday = models.DateTimeField()
    university = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Article(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")
    tags = models.ManyToManyField("Tag", related_name="articles")
    # 给一个已有数据的表添加字段时，需要设置null=True，也就是允许为空，否则会报错
    # 或者设置一个默认值，比如default=datetime.datetime.now()
    new_pub_time = models.DateTimeField(auto_now_add=True, null=True)


class Tag(models.Model):
    name = models.CharField(max_length=100, null=False)


class Comment(models.Model):
    content = models.TextField()
    origin_comment = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
