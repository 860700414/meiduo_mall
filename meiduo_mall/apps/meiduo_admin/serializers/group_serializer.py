from rest_framework import serializers

from django.contrib.auth.models import Group

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group

        fields = "__all__"
    #     A user in a group automatically has all the permissions granted to that
    #     group. For example, if the group 'Site editors' has the permission
    #     can_edit_home_page, any user in that group will have that permission.