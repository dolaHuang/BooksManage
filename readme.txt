*****************欢迎提出您宝贵的建议和批评****************

-------------------------------------------------------------图书增删改查网页版应用-v0.1
Tue Sep 04 2018 17:34:20 GMT+0800 (中国标准时间)
------------------------------
练习题名称：开发图书增删改查页面
------------------------------
练习所需知识点：HTML+CSS+jQuery+bootstrap+Django
------------------------------
练习实现的功能：1.列出图书列表、出版社列表、作者列表
		2.点击作者，会列出其出版的图书列表
		3.点击出版社，会列出旗下图书列表
		4.可以创建、修改、删除 图书、作者、出版社
		5.实现简单的登陆注册功能
----------------------------------------------------------------------------------------
***************************************使用前必知***************************************
运行环境
	1）IDE:pycharm2018.1.3专业版
		python3.6.5
		Django2.1
		pyMySQL0.9.2
		jquery3.2.1
		bootstrap3.3.7

	2）数据库软件:MySQL-->version:5.6.40

	3) 浏览器:谷歌浏览器

----------------------------------------------------------------------------------------
以下都将使用（127.0.0.1:8000/ ）演示说明

1、项目文件名：	BM；
2、主页面地址：127.0.0.1:8000/index/ ；

----------------------------------------------------------------------------------------
启动流程

1、启动数据库，创建库文件
2、设置Django数据库连接：Django项目文件夹BM----->settings----->找到DATABASES，设置数据库地址，表名，账号密码等内容
3、迁移数据库，
4、启动Django
5、插入测试数据：地址栏输入localhost:端口号/insterdata/，例如-->127.0.0.1:8000/insterdata/,程序将自动插入准备好的文本内的测试数据；
6、需自行注册账号进行登录才能正常使用，输入主页面地址127.0.0.1:8000/index/进入登录页面，点左下角注册即可进入注册页面；

----------------------------------------------------------------------------------------
项目目录

│  authorDetails 	作者详情表测试数据
│  authors	作者表从测试数据
│  book	图书测试数据
│  db.sqlite3
│  insterStaute	数据插入完成状态
│  manage.py
│  publish	出版社表测试数据	
│  
├─bm01	图书管理APP
│  │  admin.py
│  │  apps.py
│  │  as.py
│  │  login.py
│  │  models.py	表关系文件，模型层
│  │  myforms.py	自定义校验组件类
│  │  myPaginator.py	自定义分页器
│  │  tests.py
│  │  urls.py		路由分发
│  │  views.py	视图函数
│  │  __init__.py
│  │  
│  │          
│  ├─static
│  │  │  jquery-3.2.1.min.js		jquery库文件
│  │  │  session.js		jquery-session库文件
│  │  │  __init__.py
│  │  │  
│  │  ├─dist 样式库bootstrap样式库
│  │  │  ├─css
│  │  │  │      bootstrap-theme.css
│  │  │  │      bootstrap-theme.css.map
│  │  │  │      bootstrap-theme.min.css
│  │  │  │      bootstrap-theme.min.css.map
│  │  │  │      bootstrap.css
│  │  │  │      bootstrap.css.map
│  │  │  │      bootstrap.min.css
│  │  │  │      bootstrap.min.css.map
│  │  │  │      
│  │  │  ├─fonts
│  │  │  │      glyphicons-halflings-regular.eot
│  │  │  │      glyphicons-halflings-regular.svg
│  │  │  │      glyphicons-halflings-regular.ttf
│  │  │  │      glyphicons-halflings-regular.woff
│  │  │  │      glyphicons-halflings-regular.woff2
│  │  │  │      
│  │  │  └─js
│  │  │          bootstrap.js
│  │  │          bootstrap.min.js
│  │  │          npm.js
│  │  │          
│  │  └─pic		应用界面图片
│  │          1.jpg
│  │          author.png
│  │          author_l.png
│  │          backgroundimg.jpg
│  │          book.png
│  │          book_l.png
│  │          index.png
│  │          publish.png
│  │          publish_l.png
│  │          title.png
│  │          __init__.py
│  │          
│          
├─BM	
│  │  mySettings.py	自定义设置
│  │  settings.py	DJango设置
│  │  urls.py	全局路由	
│  │  wsgi.py
│  │  __init__.py
│  │  
│          
├─login01	登陆APP
│  │  admin.py
│  │  apps.py
│  │  models.py
│  │  tests.py
│  │  urls.py 	路由
│  │  views.py	视图
│  │  __init__.py
│  │  
│          
├─templates	模板文件
│      addAuthor.html	添加作者页面
│      addBook.html	添加图书
│      addPublish.html	添加出版社
│      authors.html	展示作者
│      base.html	继承样板base
│      books.html	展示图书
│      change.html	修改页面	
│      change_base.html	修改继承样板base
│      delete_model.html	删除模态框
│      index.html		主页
│      insterData.html		插入测试数据页面
│      login_reg_model.html	登陆模态框
│      publishers.html		展示出版社
│      show_base.html	展示继承样板base
│      

           
   
	









