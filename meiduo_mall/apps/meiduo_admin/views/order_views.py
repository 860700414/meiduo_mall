from rest_framework.generics import ListAPIView
from orders.models import OrderInfo
from meiduo_admin.serializers.order_serializer import OrderinfoSerializer
from meiduo_admin.pages import MyPage

class OrderInfoView(ListAPIView):
    queryset = OrderInfo.objects.all()
    serializer_class = OrderinfoSerializer
    pagination_class = MyPage
    def get_queryset(self):
        keyword=self.request.query_params.get('keyword')
        if keyword:
            return self.queryset.filter(order_id__contains=keyword)
        return self.queryset.all()