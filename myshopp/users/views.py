from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.
from . import models
from . import utils
from io import BytesIO


def user_login(request):
    if request.method == 'GET':
        try:
            next_url = request.GET['next']
        except:
            next_url = '/'
        return render(request, 'users/login.html', {'next_url': next_url})
    elif request.method == 'POST':
        username = request.POST['username'].strip()
        password = request.POST['password'].strip()
        next_url = request.POST.get('next', '/')
        # 验证码
        # code = request.POST['code']

        # User.objects.get(username=username,password=password).first()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(next_url)
            else:
                return render(request, 'users/login.html', {'error_code': 2, 'msg': '你的账号已经被锁定，请联系管理员！'})

        else:
            return render(request, 'users/login.html', {'error_code': 3, 'msg': '用户名或密码错误，请重新登录！'})


def register(request):
    if request.method == 'GET':
        return render(request, 'users/register.html', {})
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        nickname = request.POST['nickname']
        confirmpwd = request.POST['confirmpwd']

        # 验证码
        # code = request.POST['code']

        # 两次密码是否一样
        if password != confirmpwd:
            return render(request, 'users/register.html', {'error_code': 1, 'msg': '两次密码不一致，请重新输入！'})

        # 判断用户名是否可用
        try:
            User.objects.get(username=username)
            return render(request, 'users/register.html', {'error_code': 2, 'msg': '该用户已存在，请重新输入！'})
        except:
            # 判断昵称不能重复
            try:
                models.UserInfo.objects.get(nickname=nickname)
                return render(request, 'users/register.html', {'error_code': 3, 'msg': '该用户昵称已存在，请重新输入！'})

            except:

                # 保存用户信息
                user = User.objects.create_user(username=username, password=password)
                userInfo = models.UserInfo(nickname=nickname, user=user)
                user.save()
                userInfo.save()
                return render(request, 'users/login.html', {'error_code': 1, 'msg': '用户已经注册成功， 请前往登录！'})



def user_logout(request):
    logout(request)
    return render(request, 'users/login.html', {'error_code': 4, 'msg': '退出成功，请重新登录！'})


@login_required
def userinfo(request):
    return render(request, 'users/userInfo.html', {})


def createImage(request):
    # 准备空间，放置验证码图片
    i = BytesIO()
    # 生成验证码及其图片
    imge, code = utils.create_code()
    # 把验证码图片保存到流里面
    imge.save(i, 'png')
    # 方便拿过来用户的输入做验证
    request.session['code'] = code
    print(imge, code, request.session['code'])
    return HttpResponse(i.getvalue())


def register1(request):
    return render(request, 'users/register1.html')


def add_address(request):
    if request.method == "GET":
        return render(request, "users/add_address.html", {})
    else:
        recv_name = request.POST["recv_name"]
        recv_tel = request.POST["recv_tel"]
        province = request.POST["province"]
        city = request.POST["city"]
        area = request.POST["area"]
        street = request.POST["street"]
        desc = request.POST["desc"]

        try:
            # 说明这个地址设为默认
            request.POST["is_default"]
            addresses = models.Address.objects.filter(user=request.user)
            for address in addresses:
                address.is_default = False
                address.save()

            address = models.Address(recv_name=recv_name, recv_tel=recv_tel, province=province, city=city, area=area,\
                           street=street, desc=desc, user=request.user, is_default=True)
            address.save()
        except:
            address = models.Address(recv_name=recv_name, recv_tel=recv_tel, province=province, city=city, area=area, \
                                     street=street, desc=desc, user=request.user)
            address.save()

        return redirect(reverse("users:address_list"))


def address_list(request):
    addresses = models.Address.objects.filter(user=request.user)
    return render(request, "users/list_address.html", {"addresses": addresses})
