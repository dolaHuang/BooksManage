from django.shortcuts import render, HttpResponse, redirect,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from bm01 import myforms
import json


# Create your views here.

# 登陆
def login(request):
    response = {'user': None, 'msg': ''}

    if request.method == 'POST':
        userForm = myforms.UserInfoForm(request.POST)
        if userForm.is_valid():
            user = request.POST.get('username')
            pwd = request.POST.get('password')
            user_ret = auth.authenticate(username=user, password=pwd)
            if user_ret:
                auth.login(request, user_ret)
                request.session['user'] = user
                response['user'] = user
            else:
                response['msg'] = {'username': [' 账号或者密码错误'], 'password': ['账号或者密码错误']}
        else:
            response['msg'] = userForm.errors

        return HttpResponse(json.dumps(response))

    return render(request,'index.html')


# 注册
def reg(request):
    response = {'user': None, 'msg': ''}
    if request.method == 'POST':
        regForm = myforms.RegForm(request.POST)
        if regForm.is_valid():

            user = request.POST.get('username')
            pwd = request.POST.get('password')

            user_obj = User.objects.create_user(username=user, password=pwd)
            response['user'] = user

        else:
            response['msg'] = regForm.errors

        return HttpResponse(json.dumps(response))
    return redirect('/index/')

# 注销登陆
def logout_view(request):

    logout(request)

    return redirect('/index/')