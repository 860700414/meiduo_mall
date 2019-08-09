from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView


from goods.models import SKU,GoodsCategory
from meiduo_admin.pages import MyPage
from meiduo_admin.serializers.sku_serializer import SKUModelSerializer,SKUCategorySimpleSerializer


class SKUViewSet(ModelViewSet):
    queryset = SKU.objects.all()
    serializer_class = SKUModelSerializer
    pagination_class = MyPage

    def get_queryset(self):

        keyword=self.request.query_params.get('keyword')
        if keyword:
            return self.queryset.filter(name__contains=keyword)
        return self.queryset.all()
class SKUCategoryView(ListAPIView):
    queryset = GoodsCategory.objects.filter(parent_id__gt=37)
    serializer_class = SKUCategorySimpleSerializer



