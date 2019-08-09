from rest_framework import serializers
from goods.models import SKU, SKUSpecification,GoodsCategory,SPU


class SKUSpecSimpleSerializer(serializers.ModelSerializer):
    spec_id = serializers.IntegerField()
    option_id = serializers.IntegerField()

    class Meta:
        model = SKUSpecification
        fields = ['spec_id', 'option_id']


class SKUModelSerializer(serializers.ModelSerializer):
    spu = serializers.StringRelatedField()
    spu_id = serializers.IntegerField()
    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()

    specs = SKUSpecSimpleSerializer(many=True)

    class Meta:
        model = SKU
        fields = "__all__"

class SKUCategorySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = ['id','name']


