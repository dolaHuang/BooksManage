from django.shortcuts import render, redirect
from bm01.models import *
from django.core.paginator import Paginator
from bm01.myPaginator import paginator
from bm01.myforms import *
from BM3 import mySettings
import time
import datetime
import random
from login01.views import login,login_required

# Create your views here.


# 首页
def index(request):
    return render(request, 'index.html')


# 查询指定对象的所有图书功能
@login_required
def show(request, id, title):
    if title == 'publish':
        show_obi_list = Book.objects.filter(publish_id=id)
    elif title == 'author':
        show_obi_list = Book.objects.filter(author__aid=id)
    current_page, page_range = paginator(request, show_obi_list)
    # 因为是查看图书页面，所以要修改成图书
    title='图书'
    english_title='book'
    return render(request, 'books.html', locals())


# 删除
@login_required
def delete(request, id, title):
    model_dict = {
        'book': [Book, '/book/', '书籍'],
        'publish': [Publish, '/publish/', '出版社'],
        'author': [Author, '/author/', '作者']
    }
    # 一对一需要单独操作
    if title == 'author':
        AuthorDetails.objects.filter(author__aid=id).delete()
    mySettings.MODEL_DICT[title][0].objects.filter(pk=id).delete()
    return redirect(mySettings.MODEL_DICT[title][3])


# 编辑公用函数
@login_required
def change(request, id, title):
    title = title
    model_dict = {
        'book': [changeBook],
        'publish': [changePublish],
        'author': [changeAuthor]
    }
    edit_obj = mySettings.MODEL_DICT[title][0].objects.filter(pk=id).first()

    if title == 'book':
        book_author_list = [i.pk for i in edit_obj.author.all()]
    else:
        # 定义之后，防止前端JQ因为没有值而出错
        book_author_list = []
    page_theme = mySettings.MODEL_DICT[title][5]
    form = mySettings.MODEL_DICT[title][4]()
    # 修改提交后的操作
    if request.method == 'POST':
        form = mySettings.MODEL_DICT[title][4](request.POST)
        print(form.errors)
        if form.is_valid():
            print(request.POST)
            model_dict[title][0](request, id, edit_obj)
            return redirect('/%s/' % title)

    return render(request,'change.html', locals())


# 编辑书籍
@login_required
def changeBook(request, id, book_obj):
    title = request.POST.get('title')
    price = request.POST.get('price')
    authors = request.POST.getlist('author')
    year = request.POST.get('pub_data_year')
    month = request.POST.get('pub_data_month')
    day = request.POST.get('pub_data_day')
    publish = request.POST.get('publish')
    # 跟新图书信息
    Book.objects.filter(pk=id).update(title=title, price=price, pub_date='%s-%s-%s' % (year, month, day),
                                      publish_id=publish)
    # 清空多对多，再重新绑定
    book_obj.author.clear()
    book_obj.author.add(*authors)



# 编辑出版社
@login_required
def changePublish(request, id, publish_obj):
    name = request.POST.get("name")
    tel = request.POST.get("tel")
    addr = request.POST.get("addr")
    # 跟新出版社表
    Publish.objects.filter(pk=id).update(name=name, tel=tel, addr=addr)


# 编辑作者
@login_required
def changeAuthor(request, id, publish_obj):
    name = request.POST.get("name")
    birthday_month = request.POST.get('birthday_month')
    birthday_day = request.POST.get('birthday_day')
    birthday_year = request.POST.get('birthday_year')
    tel = request.POST.get('tel')
    addr = request.POST.get('addr')
    gender = request.POST.get('gender')
    # 跟新作家详情
    AuthorDetails.objects.filter(author__aid=id).update(
        birthday='%s-%s-%s' % (birthday_year, birthday_month, birthday_day),
        tel=tel, addr=addr)
    # 跟新作家表
    Author.objects.filter(pk=id).update(name=name, gender=gender)


# 添加书籍
@login_required
def addBook(request):
    if request.method == 'POST':
        bookForm = BookForm(request.POST)
        if bookForm.is_valid():
            title = request.POST.get('title')
            price = request.POST.get('price')
            authors = request.POST.getlist('author')
            year = request.POST.get('pub_data_year')
            month = request.POST.get('pub_data_month')
            day = request.POST.get('pub_data_day')
            publish = request.POST.get('publish')
            # 出版社插入数据库
            book_obj = Book.objects.create(title=title, price=price, pub_date='%s-%s-%s' % (year, month, day),
                                           publish_id=publish)
            # 书籍绑定作者
            book_obj.author.add(*authors)

            return redirect('/book/')
        else:
            return render(request, 'addBook.html', locals())
    bookForm = BookForm()

    return render(request, 'addBook.html', locals())


# 添加出版社
@login_required
def addPublish(request):
    if request.method == 'POST':
        publishForm = PublishForm(request.POST)
        if publishForm.is_valid():
            name = request.POST.get("name")
            tel = request.POST.get("tel")
            addr = request.POST.get("addr")
            # 插入数据到出版社
            obj = Publish.objects.create(name=name, tel=tel, addr=addr)

            return redirect('/publish/')
        else:
            return render(request, 'addPublish.html', locals())
    publishForm = PublishForm()
    return render(request, 'addPublish.html', locals())


# 添加作者
@login_required
def addAuthor(request):
    if request.method == 'POST':
        authorForm = AuthorForm(request.POST)
        if authorForm.is_valid():
            name = request.POST.get("name")
            birthday_month = request.POST.get('birthday_month')
            birthday_day = request.POST.get('birthday_day')
            birthday_year = request.POST.get('birthday_year')
            tel = request.POST.get('tel')
            addr = request.POST.get('addr')
            gender = request.POST.get('gender')
            # 插入作者详情
            obj_ad = AuthorDetails.objects.create(birthday='%s-%s-%s' % (birthday_year, birthday_month, birthday_day),
                                                  tel=tel, addr=addr)

            # 插入作者表
            obj_a = Author.objects.create(name=name, gender=gender, author=obj_ad)
            return redirect('/author/')

        else:
            return render(request, 'addAuthor.html', locals())

    authorForm = AuthorForm()
    return render(request, 'addAuthor.html', locals())


# 查看书籍
@login_required
def books(request):
    title = '图书'
    english_title = 'book'
    book_list = Book.objects.filter()
    current_page, page_range = paginator(request, book_list)

    return render(request, 'books.html', locals())


# 查看出版社
@login_required
def publishers(request):
    title = '出版社'
    english_title = "publish"
    publish_list = Publish.objects.filter()
    current_page, page_range = paginator(request, publish_list)
    return render(request, 'publishers.html', locals())


# 查看作者
@login_required
def authors(request):
    title = '作者'
    english_title = 'author'
    # AuthorDetails
    author_list = Author.objects.filter().values('aid', 'name', 'gender', 'author__birthday', "author__tel",
                                                 'author__addr')
    current_page, page_range = paginator(request, author_list)

    return render(request, 'authors.html', locals())


# 打开文件
def fileOpen(filename):
    return


# 插入测试数据函数
def insterData(request):
    # 捕捉异常
    with open('insterStaute', 'r') as f:
        data = f.read()
    if len(data):
        msg = '测试数据已添加'
        path = ''
        return render(request, 'insterData.html', locals())
    else:
        print(time.time())
        # 插入作者详情
        authorsDetatils_list = []
        with open('authorDetails', 'r', encoding='utf8') as f:
            for line in f:
                line_list = line.split()

                authorsDetatil = AuthorDetails(birthday=line_list[2], tel=line_list[4], addr=line_list[3])
                authorsDetatils_list.append(authorsDetatil)
        AuthorDetails.objects.bulk_create(authorsDetatils_list)

        # 插入作者
        author_list = []
        with open('authors', 'r', encoding='utf8') as f:
            i = 0
            for line in f:
                i += 1
                line_list = line.split()

                author = Author(name=line_list[1], gender=line_list[2], author_id=i)
                author_list.append(author)
        Author.objects.bulk_create(author_list)

        #  插入出版社
        publish_list = []
        with open('publish', 'r', encoding='utf8') as f:
            for line in f:
                line_list = line.split()

                publish = Publish(name=line_list[1], tel=line_list[3], addr=line_list[2])
                publish_list.append(publish)
        Publish.objects.bulk_create(publish_list)

        # 插入图书
        with open('book', 'r', encoding='utf8') as f:

            for line in f:
                i = random.randrange(1, len(author_list))
                line_list = line.split()

                book_obj = Book.objects.create(title=line_list[1], price=float(line_list[2]), pub_date=line_list[3],
                                               publish_id=random.randrange(1, len(publish_list)))
                author_obj = Author.objects.filter(author_id=i).first()
                book_obj.author.add(author_obj)
        with open('insterStaute', 'w',encoding='utf8') as f:
            f.write('添加完成！')
        msg = "测试数据插入成功!"
        path = ''
        print(time.time())
        return render(request, 'insterData.html', locals())



