#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/31 22:28
# @Author  : DollA
# @Site    : 
# @File    : myforms.py
# @Software: PyCharm
from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError

#####################自定义filed下拉选项#######################
import datetime

# 自定义月和日选项

MONTHS_b = MONTHS_a = [i for i in range(1, 13)]

MONTHS = dict(zip(MONTHS_a, MONTHS_b))

# 自定义年选项
this_year = datetime.date.today().year
YEAR = range(this_year - 100, this_year + 1)

# 自定义出版社和作者下拉菜单
# 出版社select选项
"""
    publish_list = Publish.objects.all()
    publish_id_list = [i.pid for i in publish_list]
    publish_name_list = [i.name for i in publish_list]
    PUBLISHS = list(zip(publish_id_list, publish_name_list))
    # 作者多选框
    author_list = Author.objects.all()
    author_id_list = [i.aid for i in author_list]
    author_name_list = [i.name for i in author_list]
    AUTHORS = list(zip(author_id_list, author_name_list))
else:
    # 从本地取值
    AUTHORS=''
    PUBLISHS=''
"""
author_name_list = []
author_id_list = []
i=0
with open('authors', 'r', encoding='utf8') as f:
    for line in f:
        i+=1
        line_list = line.split()
        author_name_list.append(line_list[1])
        author_id_list.append(i)

AUTHORS = list(zip(author_id_list, author_name_list))

publish_id_list = []
publish_name_list = []
j=0
with open('publish','r',encoding='utf8') as f:
    for line in f:
        j+=1
        line_list =line.split()
        publish_name_list.append(line_list[1])
        publish_id_list.append(j)
PUBLISHS = list(zip(publish_id_list, publish_name_list))
################################################################


# 图书FORMS
class BookForm(forms.Form):
    title = forms.CharField(min_length=1, label='图书名称', error_messages={'required': '图书名称不能为空'},
                            widget=widgets.TextInput(attrs={'class': 'form-control'}))
    price = forms.DecimalField(decimal_places=2, label='图书价格',
                               error_messages={'required': '图书价格不能为空', 'invalid': '请输入数字'},
                               widget=widgets.TextInput(attrs={'class': 'form-control'}))
    author = forms.MultipleChoiceField(choices=AUTHORS, label='作者', error_messages={'required': '作者不能为空'},
                                       widget=widgets.SelectMultiple(attrs={'class': 'form-control'}))
    pub_data = forms.DateField(label='出版日期', error_messages={'required': '日期不能为空'},
                               widget=widgets.SelectDateWidget(months=MONTHS, years=YEAR,
                                                               attrs={'class': 'form-control'}))
    publish = forms.ChoiceField(label='出版社名称', choices=PUBLISHS, error_messages={'required': '图书名称不能为空'},
                                widget=widgets.Select(attrs={'class': 'form-control'}))

    def clean_price(self):
        val = self.cleaned_data.get('price')
        if val < 0:
            raise ValidationError('价格不能为负数')
        else:
            return val


# 作者form组件
class AuthorForm(forms.Form):
    name = forms.CharField(min_length=2, label='作家姓名',
                           error_messages={'required': '姓名不能为空', 'min_length': '姓名不能小于2个字符'},
                           widget=widgets.TextInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(label='性别', choices=[('男', '男'), ('女', '女')],
                               error_messages={'required': '性别不能为空'},
                               widget=widgets.Select(attrs={'class': 'form-control'}))
    birthday = forms.DateField(label='出生日期', error_messages={'required': '出生日期不能为空'},
                               widget=widgets.SelectDateWidget(months=MONTHS, years=YEAR,
                                                               attrs={'class': 'form-control'}))
    tel = forms.CharField(label='电话', error_messages={'required': '电话不能为空'},
                          widget=widgets.TextInput(attrs={'class': 'form-control'}))
    addr = forms.CharField(min_length=2, label='地址', error_messages={'required': '地址不能为空', 'min_length': '地址不能小于4个字符'},
                           widget=widgets.TextInput(attrs={'class': 'form-control'}))

    def clean_tel(self):
        val = self.cleaned_data.get('tel')
        if len(val) == 11 and val.isdigit():
            return val
        else:
            raise ValidationError('请输入11位电话号码')

    def clean_name(self):
        val = self.cleaned_data.get('name')
        if not val.isdigit():
            return val
        else:
            raise ValidationError('姓名不能是纯数字')

    def clean_addr(self):
        val = self.cleaned_data.get('addr')
        if not val.isdigit():
            return val
        else:
            raise ValidationError('地址不能是纯数字')


# 出版社form组件
class PublishForm(forms.Form):
    name = forms.CharField(min_length=5, label='出版社名称',
                           error_messages={'required': '出版社名称不能为空', 'min_length': '名称不能小于5个字符'},
                           widget=widgets.TextInput(attrs={'class': 'form-control'}))
    tel = forms.CharField(label='电话', error_messages={'required': '电话不能为空'},
                          widget=widgets.TextInput(attrs={'class': 'form-control'}))
    addr = forms.CharField(min_length=4, label='地址', error_messages={'required': '地址不能为空', 'min_length': '地址不能小于4个字符'},
                           widget=widgets.TextInput(attrs={'class': 'form-control'}))

    def clean_tel(self):
        val = self.cleaned_data.get('tel')
        if len(val) == 7 or len(val) == 11 and val.isdigit():
            return val
        else:
            raise ValidationError('请输入7位电话号码')

    def clean_name(self):
        val = self.cleaned_data.get('name')
        if not val.isdigit():
            return val
        else:
            raise ValidationError('名称不能是纯数字')

    def clean_addr(self):
        val = self.cleaned_data.get('addr')
        if not val.isdigit():
            return val
        else:
            raise ValidationError('地址不能是纯数字')


# # 用户信息forms组件
class UserInfoForm(forms.Form):
    username = forms.CharField(min_length=4, error_messages={'required': '出版社名称不能为空', 'min_length': '用户名不能小于4个字符'})
    password = forms.CharField(min_length=6, error_messages={'required': '出版社名称不能为空', 'min_length': '密码不能小于6个字符'})


class RegForm(forms.Form):
    username = forms.CharField(max_length=32, min_length=4,
                               widget=widgets.TextInput(attrs={"class": "form-control"}),
                               error_messages={"required": "用户不能为空", "min_length": "用户名最小长度4位"})
    password = forms.CharField(min_length=6, widget=widgets.PasswordInput(attrs={"class": "form-control"}),
                               error_messages={"required": "密码不能为空",
                                               "min_length": "密码最小长度6位",
                                               })
    password_r = forms.CharField(widget=widgets.PasswordInput(attrs={"class": "form-control"}),
                                 error_messages={"required": "密码不能为空", "min_length": "密码最小长度6位", })

    def clean(self):
        pwd = self.cleaned_data.get("password")
        pwd_r = self.cleaned_data.get("password_r")
        if pwd and pwd_r:
            if pwd == pwd_r:
                return self.cleaned_data
            else:
                raise ValidationError("两次密码不一致")
        else:
            return self.cleaned_data


bookform = BookForm()
print(bookform.__dict__)
