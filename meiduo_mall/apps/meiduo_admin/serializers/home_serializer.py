from rest_framework import serializers

from goods.models import GoodsVisitCount


class GoodsVisitCountSerializer():
    category=serializers.StringRelatedField()

    class Meta:
        model =GoodsVisitCount
        fields=['category','count']