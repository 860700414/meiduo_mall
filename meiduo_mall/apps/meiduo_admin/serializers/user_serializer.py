from users.models import User

from rest_framework import serializers
from django.contrib.auth.hashers import make_password
# 对数据及进行分页
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['id','username','mobile','email','password']
        extra_kwargs ={'password':{'write_only':True}}

    def create(self, validated_data):
        return User.objects.create_superuser(**validated_data)
    # def create(self, validated_data):
    #     password=validated_data['password']
    #     validated_data['password']= make_password(password)
    #     validated_data['is_staff']=True
    #     return super(UserDetailSerializer, self).create(validated_data)

