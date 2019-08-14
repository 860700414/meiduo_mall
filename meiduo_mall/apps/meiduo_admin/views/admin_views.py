from meiduo_admin.serializers.admin_serializer import AdminUserSerializer
from meiduo_admin.serializers.group_serializer import GroupSerializer
from users.models import User
from django.contrib.auth.models import Group
from meiduo_admin.pages import MyPage
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView


class AdminUserViewSet(ModelViewSet):
    queryset = User.objects.filter(is_staff=True)
    serializer_class = AdminUserSerializer
    pagination_class = MyPage


class GroupSimpleView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
