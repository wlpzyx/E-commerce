"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = 2019/3/19
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^myorder/(\d+)/$',views.myorder, name='myorder'),
    url(r'^orderlist/$',views.orderlist, name='orderlist'),
    url(r'^orderdetail/(\d+)/$',views.orderdetail, name='orderdetail'),
    url(r'^del_order/(\d+)/$',views.del_order, name='del_order'),
]