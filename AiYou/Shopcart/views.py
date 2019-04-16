from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse, HttpResponse
from Goods.models import Goods
from MyOrder.models import OrderItem, Order
from Users.models import Address
from . import models


def add_shopcart(request):
    """
    ajax添加购物车
    :param request:
    :return:
    """
    goods_id = request.GET['goods_id']
    price = Goods.objects.get(pk=goods_id).price
    num = request.GET['num']
    subtotal = int(price)*int(num)
    # 判断购物车里是否有此商品
    shopcart = models.Shopcart.objects.filter(goods_id=goods_id)
    if len(shopcart) > 0:
        num = int(shopcart[0].count)+int(num)
        subtotal = int(shopcart[0].subtotal)+subtotal
        shopcart[0].count, shopcart[0].subtotal = num, subtotal
        shopcart[0].save()
    else:
        models.Shopcart(count=num, subtotal=subtotal, goods_id=goods_id, users=request.user).save()
    return JsonResponse({"a":'添加成功!'})


def del_shopcart(request):
    """
    ajax删除购物车
    :param request:
    :return:
    """
    # 删除
    shopcars_id = request.GET.get('shopcars_id').split(',')
    models.Shopcart.objects.filter(id__in=shopcars_id).delete()
    # 购物车总价格
    stopcars = models.Shopcart.objects.filter(users=request.user)
    resault = 0
    for i in stopcars:
        resault += int(i.subtotal)
    return JsonResponse({'a':resault})


def shopcars(request):
    """
    购物车类列表
    :param request:
    :return:
    """
    if request.method == 'GET':
        stopcars = models.Shopcart.objects.filter(users=request.user)
        # 购物车总价格
        resault = 0
        for i in stopcars:
            resault += int(i.subtotal)
        return render(request, 'shopcart/shopcars.html', {'stopcars':stopcars, 'resault':resault})
    if request.method == 'POST':
        storecars_id = request.POST.getlist('storecars_id')
        img = request.POST.get('img')
        try:
            addr_obj = Address.objects.filter(users=request.user, status='1')[0]
            addr_def = addr_obj.province + addr_obj.city+addr_obj.country + addr_obj.desc
            order = Order(recv_name=request.user.users.mickname, recv_address=addr_def,
                                 recv_phone=request.user.users.phone, totale=0, user=request.user)
            order.save()
        except:
            order = Order(recv_name=request.user.users.mickname, recv_address='',
                          recv_phone=request.user.users.phone, totale=0, user=request.user)
            order.save()
        totale = 0
        for i in storecars_id:
            shopcart = models.Shopcart.objects.get(pk=i)
            OrderItem(oi_goods_id=shopcart.goods_id, oi_goods_image_path=img, oi_goods_name=shopcart.goods.name,
                             oi_goods_price=shopcart.goods.price, oi_goods_count=shopcart.count,
                             deal_price=shopcart.subtotal, order=order).save()
            models.Shopcart.objects.get(pk=i).delete()
            totale += shopcart.subtotal
        order.totale = totale
        order.save()
        # return redirect(reverse('myorder:orderdetail', args=(order.id,)))
        return redirect(reverse('myorder:orderlist'))