from rest_framework import serializers
from goods.models import SPU, Brand, GoodsCategory


class SPUDetailSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    brand_id = serializers.IntegerField()

    # 除隐含字段 模型类序列化器关联的外键需要指明
    category1_id = serializers.IntegerField()
    category2_id = serializers.IntegerField()
    category3_id = serializers.IntegerField()

    class Meta:
        model = SPU
        fields = "__all__"

        # exclude= ['category1','category2','category3']
        extra_kwargs = {
            'category1': {'read_only': True},
            'category2': {'read_only': True},
            'category3': {'read_only': True}

        }


class BrandSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']


class GoodsCategorySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = ['id', 'name']

