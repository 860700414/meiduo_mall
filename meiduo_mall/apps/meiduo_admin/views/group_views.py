from rest_framework.viewsets import ModelViewSet
from meiduo_admin.serializers.group_serializer import GroupSerializer
from django.contrib.auth.models import Group
from meiduo_admin.pages import MyPage

class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = MyPage
