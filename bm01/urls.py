#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path,re_path
from bm01 import views

urlpatterns = [
    # 插入数据
    path('insterdata/', views.insterData),
    # 主页
    path('index/', views.index),
    # 修改数据
    path('changebook/', views.changeBook),
    path('<str:title>/<int:id>/change', views.change),
    # 添加数据
    path('addbook/', views.addBook),
    path('addauthor/', views.addAuthor),
    path('addpublish/', views.addPublish),
    # 查看当前类列表
    path('publish/', views.publishers),
    path('book/', views.books),
    path('author/', views.authors),
    # 删除数据
    path('<str:title>/<int:id>/delete/', views.delete),
    # 查看点击范围数据
    path('<str:title>/<int:id>/show/', views.show),
    # re_path('/login/',views.login)

]
