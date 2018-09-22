from django.db import models


# Create your models here.
# 出版社表
class Publish(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    tel = models.CharField(max_length=11, unique=True)
    addr = models.CharField(max_length=32)


# 作者详情
class AuthorDetails(models.Model):
    adid = models.AutoField(primary_key=True)
    birthday = models.DateField()
    tel = models.BigIntegerField()
    addr = models.CharField(max_length=64)


# 作者表
class Author(models.Model):
    aid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    gender = models.CharField(max_length=5)
    # 一对一关联作者详细表
    author = models.OneToOneField(to='AuthorDetails', on_delete=models.CASCADE)


# 图书表
class Book(models.Model):
    bid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    pub_date = models.DateField()

    # 一对多关联出版社
    publish = models.ForeignKey(to="Publish", to_field='pid', on_delete=models.CASCADE)
    # 多对多关联作者
    author = models.ManyToManyField(to='Author')


# 用户信息表
