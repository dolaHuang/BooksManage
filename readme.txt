*****************��ӭ���������Ľ��������****************

-------------------------------------------------------------ͼ����ɾ�Ĳ���ҳ��Ӧ��-v0.1
Tue Sep 04 2018 17:34:20 GMT+0800 (�й���׼ʱ��)
------------------------------
��ϰ�����ƣ�����ͼ����ɾ�Ĳ�ҳ��
------------------------------
��ϰ����֪ʶ�㣺HTML+CSS+jQuery+bootstrap+Django
------------------------------
��ϰʵ�ֵĹ��ܣ�1.�г�ͼ���б��������б������б�
		2.������ߣ����г�������ͼ���б�
		3.��������磬���г�����ͼ���б�
		4.���Դ������޸ġ�ɾ�� ͼ�顢���ߡ�������
		5.ʵ�ּ򵥵ĵ�½ע�Ṧ��
----------------------------------------------------------------------------------------
***************************************ʹ��ǰ��֪***************************************
���л���
	1��IDE:pycharm2018.1.3רҵ��
		python3.6.5
		Django2.1
		pyMySQL0.9.2
		jquery3.2.1
		bootstrap3.3.7

	2�����ݿ����:MySQL-->version:5.6.40

	3) �����:�ȸ������

----------------------------------------------------------------------------------------
���¶���ʹ�ã�127.0.0.1:8000/ ����ʾ˵��

1����Ŀ�ļ�����	BM��
2����ҳ���ַ��127.0.0.1:8000/index/ ��

----------------------------------------------------------------------------------------
��������

1���������ݿ⣬�������ļ�
2������Django���ݿ����ӣ�Django��Ŀ�ļ���BM----->settings----->�ҵ�DATABASES���������ݿ��ַ���������˺����������
3��Ǩ�����ݿ⣬
4������Django
5������������ݣ���ַ������localhost:�˿ں�/insterdata/������-->127.0.0.1:8000/insterdata/,�����Զ�����׼���õ��ı��ڵĲ������ݣ�
6��������ע���˺Ž��е�¼��������ʹ�ã�������ҳ���ַ127.0.0.1:8000/index/�����¼ҳ�棬�����½�ע�ἴ�ɽ���ע��ҳ�棻

----------------------------------------------------------------------------------------
��ĿĿ¼

��  authorDetails 	����������������
��  authors	���߱�Ӳ�������
��  book	ͼ���������
��  db.sqlite3
��  insterStaute	���ݲ������״̬
��  manage.py
��  publish	��������������	
��  
����bm01	ͼ�����APP
��  ��  admin.py
��  ��  apps.py
��  ��  as.py
��  ��  login.py
��  ��  models.py	���ϵ�ļ���ģ�Ͳ�
��  ��  myforms.py	�Զ���У�������
��  ��  myPaginator.py	�Զ����ҳ��
��  ��  tests.py
��  ��  urls.py		·�ɷַ�
��  ��  views.py	��ͼ����
��  ��  __init__.py
��  ��  
��  ��          
��  ����static
��  ��  ��  jquery-3.2.1.min.js		jquery���ļ�
��  ��  ��  session.js		jquery-session���ļ�
��  ��  ��  __init__.py
��  ��  ��  
��  ��  ����dist ��ʽ��bootstrap��ʽ��
��  ��  ��  ����css
��  ��  ��  ��      bootstrap-theme.css
��  ��  ��  ��      bootstrap-theme.css.map
��  ��  ��  ��      bootstrap-theme.min.css
��  ��  ��  ��      bootstrap-theme.min.css.map
��  ��  ��  ��      bootstrap.css
��  ��  ��  ��      bootstrap.css.map
��  ��  ��  ��      bootstrap.min.css
��  ��  ��  ��      bootstrap.min.css.map
��  ��  ��  ��      
��  ��  ��  ����fonts
��  ��  ��  ��      glyphicons-halflings-regular.eot
��  ��  ��  ��      glyphicons-halflings-regular.svg
��  ��  ��  ��      glyphicons-halflings-regular.ttf
��  ��  ��  ��      glyphicons-halflings-regular.woff
��  ��  ��  ��      glyphicons-halflings-regular.woff2
��  ��  ��  ��      
��  ��  ��  ����js
��  ��  ��          bootstrap.js
��  ��  ��          bootstrap.min.js
��  ��  ��          npm.js
��  ��  ��          
��  ��  ����pic		Ӧ�ý���ͼƬ
��  ��          1.jpg
��  ��          author.png
��  ��          author_l.png
��  ��          backgroundimg.jpg
��  ��          book.png
��  ��          book_l.png
��  ��          index.png
��  ��          publish.png
��  ��          publish_l.png
��  ��          title.png
��  ��          __init__.py
��  ��          
��          
����BM	
��  ��  mySettings.py	�Զ�������
��  ��  settings.py	DJango����
��  ��  urls.py	ȫ��·��	
��  ��  wsgi.py
��  ��  __init__.py
��  ��  
��          
����login01	��½APP
��  ��  admin.py
��  ��  apps.py
��  ��  models.py
��  ��  tests.py
��  ��  urls.py 	·��
��  ��  views.py	��ͼ
��  ��  __init__.py
��  ��  
��          
����templates	ģ���ļ�
��      addAuthor.html	�������ҳ��
��      addBook.html	���ͼ��
��      addPublish.html	��ӳ�����
��      authors.html	չʾ����
��      base.html	�̳�����base
��      books.html	չʾͼ��
��      change.html	�޸�ҳ��	
��      change_base.html	�޸ļ̳�����base
��      delete_model.html	ɾ��ģ̬��
��      index.html		��ҳ
��      insterData.html		�����������ҳ��
��      login_reg_model.html	��½ģ̬��
��      publishers.html		չʾ������
��      show_base.html	չʾ�̳�����base
��      

           
   
	









