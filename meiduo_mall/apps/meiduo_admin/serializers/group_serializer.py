from rest_framework import serializers

from django.contrib.auth.models import Group

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group

        fields = "__all__"
    #     A user in a group automatically has all the permissions granted to that
    #     group. For example, if the group 'Site editors' has the permission
    #     can_edit_home_page, any user in that group will have that permission.



    # def create(self, validated_data):
    #     # 手动使用manytomanyField字段,实现创建中间表数据
    #     permissions=validated_data.pop('permissions')
    #
    #     # 1.新建的分组对象优先创建
    #     instance= self.Meta.model.objects.create(**permissions)
    #
    #     # 2\再创建中间表数据
    #     # instance.permissions= permissions
    #     instance.permissions.set(permissions)
    #     instance.save()
    #     return instance