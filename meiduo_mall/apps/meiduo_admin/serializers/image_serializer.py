from django.conf import settings
from fdfs_client.client import Fdfs_client
from rest_framework import serializers

from goods.models import SKUImage, SKU


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKUImage
        fields = ['id', 'sku', 'image']

    def validate(self, attrs):
        file_content = attrs.pop('image').read()
        res = Fdfs_client(settings.FDFS_CONF_PATH).upload_by_buffer(file_content)
        if res.get('Status') != 'Upload successed.' or not res:
            return serializers.ValidationError('图片上传失败')
        attrs['image'] = res.get('Remote file_id')
        return attrs


class SKUSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = ['id', 'name']

# class ImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SKUImage
#         fields = ['id', 'sku', 'image']

# def create(self, validated_data):
#     # 手动调用fdfs客户端程序上传图片,到分布式fdfs存储中
#     # 获得返回的file_id,mysql中存储到就是文件的id
#
#     # 1.获得浏览器传过来的数据
#
#     # file =validated_data.get('image')
#     file = validated_data.pop('image')
#     file_content = file.read()
#
#     # 2.通过fdfs客户端程序来完成文件上传
#     conn = Fdfs_client(settings.FDFS_CONF_PATH)
#     res = conn.upload_by_buffer(file_content)
#
#     if res.get('Status') != 'Upload successed.' or not res:
#         raise serializers.ValidationError('文件上传失败')
#     file_id = res.get('Remote file_id')
#     # 3.构建模型类对象保存musql数据库
#     validated_data['image'] = file_id
#     return super(ImageSerializer, self).create(validated_data)
#
# def update(self, instance, validated_data):
#     file = validated_data.pop('image')
#     file_content=file.read()
#     conn=Fdfs_client(settings.FDFS_CONF_PATH)
#     res=conn.upload_by_buffer(file_content)
#     if res.get('Status') != 'Upload successed.' or not res:
#         raise serializers.ValidationError('文件上传失败')
#     file_id= res.get('Remote file_id')
#     validated_data['image'] = file_id
#     return super(ImageSerializer, self).update(instance,validated_data)
# 重写方法
# def validate(self, attrs):
#     file= attrs.pop('image')
#     file_content=file.read()
#     conn=Fdfs_client(settings.FDFS_CONF_PATH)
#     res= conn.upload_by_buffer(file_content)
#
#     if res.get('Status') !='Upload successed.' or not res:
#         return serializers.ValidationError('图片上传失败')
#     file_id=res.get('Remote file_id')
#     attrs['image']=file_id
#     return attrs
