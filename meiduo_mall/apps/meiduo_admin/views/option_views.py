from goods.models import SpecificationOption
from meiduo_admin.serializers.option_serializer import OptionSerializer
from rest_framework.viewsets import ModelViewSet
from meiduo_admin.pages import MyPage


class OptionViewSet(ModelViewSet):
    queryset = SpecificationOption.objects.all()
    serializer_class = OptionSerializer
    pagination_class = MyPage

