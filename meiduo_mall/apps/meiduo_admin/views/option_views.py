from goods.models import SpecificationOption, SPUSpecification
from meiduo_admin.serializers.option_serializer import OptionSerializer, OptSpecSimpleSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from meiduo_admin.pages import MyPage


class OptionViewSet(ModelViewSet):
    queryset = SpecificationOption.objects.all()
    serializer_class = OptionSerializer
    pagination_class = MyPage


class OptSpecView(ListAPIView):
    queryset = SpecificationOption.objects.all()
    serializer_class = OptSpecSimpleSerializer
