from meiduo_admin.pages import MyPage
from meiduo_admin.serializers.user_serializer import *
from rest_framework.generics import ListAPIView, CreateAPIView


# from rest_framework.generics import GenericAPIView
# from rest_framework.response import Response
# from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class UserAPIView(ListAPIView, CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    pagination_class = MyPage

    # 如果前端传来了keyword，我就过滤
    # 否则默认返回默认的所有的数据集
    def get_queryset(self):
        keyword = self.request.query_params.get('keyword')
        if keyword:
            return self.queryset.filter(username__contains=keyword)
        return self.queryset.all()
