from rest_framework import serializers
from orders.models import OrderInfo, OrderGoods, SKU


class OrderInfoSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(label='创建时间', read_only=True, format='%Y-%m-%d')

    class Meta:
        model = OrderInfo
        fields = ['order_id', 'create_time']


class SKUSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = ['name', 'default_image']


class OrderGoodsSimpleSerializer(serializers.ModelSerializer):
    sku = SKUSimpleSerializer()

    class Meta:
        model = OrderGoods
        fields = ['count', 'price', 'sku']


class OrderInfoDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    skus = OrderGoodsSimpleSerializer(many=True)

    class Meta:
        model = OrderInfo
        fields = '__all__'
