from django.shortcuts import render, HttpResponse, redirect, reverse
from Goods.models import GoodsType
from Users.models import User, Address
from Shopcart.models import Shopcart
from Goods.models import GoodsType
from . import models


def orderlist(request):
    """
    订单列表
    :param request:
    :return:
    """
    orders = models.Order.objects.filter(user=request.user)
    goodstype = GoodsType.objects.filter(null_id=None)
    if len(orders) == 0:
        return render(request, 'myorder/MyCenterMyOrder.html', {'goodstype':goodstype})
    else:
        return render(request, 'myorder/OrderList.html', {'orders':orders, 'goodstype':goodstype})


def del_order(request, orderitem_id):
    """
    删除订单
    :param request:
    :param orderitem_id:
    :return:
    """
    models.OrderItem.objects.get(pk=orderitem_id).delete()
    return redirect(reverse('myorder:orderlist'))




def myorder(request, orderitem_id):
    """
    确认订单
    :param request:
    :return:
    """
    if request.method == 'GET':
        # storecars_id = request.GET.getlist('storecars_id')
        # num = request.GET.getlist('num')
        # print(storecart_id, num)
        # shopcars = Shopcart.objects.filter(pk__in=storecars_id)
        orderitem = models.OrderItem.objects.get(pk=orderitem_id)
        address = Address.objects.all()
        goodstype = GoodsType.objects.filter(null_id=None)
        return render(request, 'myorder/MyOrder.html', {'orderitem':orderitem,'address':address, 'goodstype':goodstype})
    if request.method == 'POST':
        try:
            addr_def = request.POST.get('addr_def')
            orderitem = models.OrderItem.objects.get(pk=orderitem_id)
            myorder = orderitem.order
            myorder.recv_address = addr_def
            myorder.save()
            return render(request, 'myorder/MyOrderDetail.html', {'orderitem': orderitem, 'myorder': myorder})
        except:
            return redirect(reverse('myorder:myorder', args=(orderitem_id,)))


def orderdetail(request, orderitem_id):
    """
    支付
    :param request:
    :param order_id:
    :return:
    """
    addr_def = request.POST.get('addr_def')
    orderitem = models.OrderItem.objects.get(pk=orderitem_id)
    myorder = orderitem.order
    return render(request, 'myorder/MyOrderDetail.html', {'orderitem':orderitem, 'myorder':myorder})