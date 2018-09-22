#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 11:17
# @Author  : DollA
# @Site    : 
# @File    : mySettings.py
# @Software: PyCharm
from bm01.myforms import *
from bm01 import views, models
MODEL_DICT = {
    'book': [models.Book, 'change.html', 'books.html', '/book/', BookForm, '书籍'],
    'publish': [models.Publish, 'change.html', 'publishers.html', '/publish/',PublishForm, '出版社'],
    'author': [models.Author, 'change.html', 'authors.html', '/author/', AuthorForm, '作者']
}


