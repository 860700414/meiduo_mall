from meiduo_admin.serializers.spu_serializer import *
from meiduo_admin.pages import MyPage

from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView


class SPUViewSet(ModelViewSet):
    queryset = SPU.objects.all()
    serializer_class = SPUDetailSerializer
    pagination_class = MyPage


class BrandsSimpleView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSimpleSerializer


class GoodsCategorySimpleView(ListAPIView):
    queryset = GoodsCategory.objects.all()
    serializer_class = GoodsCategorySimpleSerializer

    def get_queryset(self):
        parent_id = self.kwargs.get('pk')
        if not parent_id:
            return self.queryset.filter(parent_id=None)
        return self.queryset.filter(parent_id=parent_id)
