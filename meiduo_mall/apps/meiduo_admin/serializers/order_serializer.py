from rest_framework import serializers
from orders.models import OrderInfo


class OrderinfoSerializer(serializers.ModelSerializer):

    create_time =serializers.DateTimeField(label="创建时间",read_only=True,format='%Y %m %d')

    class Meta:
        model = OrderInfo
        fields = ['order_id', 'create_time']
