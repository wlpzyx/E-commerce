from django.db import models
from django.contrib.auth.models import User


# 订单Order
class Order(models.Model):
    # 订单编号
    id = models.AutoField(primary_key=True, verbose_name='订单编号')
    # 下单时间
    order_time = models.DateTimeField(auto_now_add=True, verbose_name='下单时间')
    # 所属用户
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='所属用户')
    # 收货人
    recv_name = models.CharField(max_length=255, verbose_name='收货人')
    # 收货地址
    recv_address = models.CharField(max_length=255, verbose_name='收货地址')
    # 联系方式
    recv_phone = models.CharField(max_length=50, verbose_name='联系方式')
    # 备注信息：
    recv_remark = models.TextField(null=True, blank=True, verbose_name='备注信息')
    # 总计金额
    totale = models.IntegerField(verbose_name='总计金额')


class OrderItem(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='订单单项id')
    oi_goods_id = models.CharField(max_length=100, verbose_name='购买商品编号')
    oi_goods_image_path = models.CharField(max_length=255, verbose_name='购买商品图片')
    oi_goods_name = models.CharField(max_length=255, verbose_name='购买商品名称')
    oi_goods_price = models.IntegerField(verbose_name='购买商品单价')
    oi_goods_count = models.IntegerField(verbose_name='购买商品数量')
    deal_price = models.IntegerField(verbose_name='成交价格')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='所属订单')
