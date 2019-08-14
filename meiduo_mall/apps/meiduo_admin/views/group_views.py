from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from meiduo_admin.serializers.group_serializer import GroupSerializer
from meiduo_admin.serializers.perms_serializer import PermSerializer
from django.contrib.auth.models import Group,Permission
from meiduo_admin.pages import MyPage

class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = MyPage
class PermissionView(ListAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermSerializer
