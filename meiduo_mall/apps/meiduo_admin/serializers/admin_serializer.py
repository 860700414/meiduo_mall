from rest_framework import serializers
from users.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.hashers import make_password

class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id',
                  'username',
                  'email',
                  'mobile',

                  'groups',
                  'user_permissions',
                  'password',
                  ]
        # password 仅仅作用于反序列化,只允许前台向后台传递密码password
        extra_kwargs={
            'password':{'write_only':True}
        }
    def validate(self, attrs):
        attrs['password']=make_password(attrs['password'])
        attrs['is_staff']=True
        return attrs