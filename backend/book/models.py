from django.db import models
from datetime import datetime


# Create your models here.
class BookModel(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name="书名")
    author = models.CharField(max_length=100, null=False)
    pub_time = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(default=0)

    class Meta:
        db_table = "book_table"
        ordering = ["price"]


class Author(models.Model):
    is_active = models.BooleanField(default=True)
    username = models.CharField(max_length=100, null=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=100, null=False)
    visit_count = models.IntegerField(default=0)
    profile = models.TextField()
    website = models.URLField()


class Tags(models.Model):
    Tags_id = models.CharField(max_length=100, default=1, null=False, primary_key=True)
    name = models.CharField(
        max_length=100, null=False, db_column="tag_name", unique=True
    )
    create_time = models.DateTimeField(default=datetime.now)
