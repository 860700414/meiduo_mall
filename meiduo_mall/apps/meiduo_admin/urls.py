from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
from meiduo_admin.views.home_views import *

from rest_framework.routers import SimpleRouter

from meiduo_admin.views.spu_views import *
from meiduo_admin.views.user_views import *
from meiduo_admin.views.sku_views import *
from meiduo_admin.views.spec_views import *
from meiduo_admin.views.option_views import *
from meiduo_admin.views.image_views import *
from meiduo_admin.views.order_views import *

urlpatterns = [
    # url(r'^authorizations/$',LoginView.as_view()),
    url(r'^authorizations/$', obtain_jwt_token),
    # url(r'^statistical/total_count/$',HomeView.as_view({'get':'total_count'})),
    # url(r'^statistical/day_increment/$',HomeView.as_view({'get':'day_increment'})),
    # url(r'^statistical/day_active/$',HomeView.as_view({'get':'day_active'})),
    url(r'^statistical/goods_day_views/$', GoodsVisitCountView.as_view()),

    url(r'^users/$', UserAPIView.as_view()),

    url(r'^skus/$', SKUViewSet.as_view({'get': 'list', 'post': 'create'})),
    url(r'^skus/(?P<pk>\d+)/$', SKUViewSet.as_view({'get': 'retrieve',
                                                    'put': 'update',
                                                    'delete': 'destroy'})),

    url(r'^skus/categories/$', SKUCategoryView.as_view()),

    url(r'^goods/simple/$', SPUSimpleView.as_view()),
    url(r'^goods/(?P<pk>\d+)/specs/$', SPUSpecView.as_view()),

    url(r'^goods/$', SPUViewSet.as_view({'get': 'list', 'post': 'create'})),
    url(r'^goods/(?P<pk>\d+)/$', SPUViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                     'delete': 'destroy'})),
    url(r'^goods/brands/simple/$', BrandsSimpleView.as_view()),

    url(r'^goods/channel/categories/$', GoodsCategorySimpleView.as_view()),
    url(r'^goods/channel/categories/(?P<pk>\d+)/$', GoodsCategorySimpleView.as_view()),

    url(r'^goods/specs/$', SpecViewSet.as_view({'get': 'list', 'post': 'create'})),
    url(r'^goods/specs/(?P<pk>\d+)/$', SpecViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                            'delete': 'destroy'})),
    url(r'^specs/options/$', OptionViewSet.as_view({'get': 'list', 'post': 'create'})),
    url(r'^specs/options/(?P<pk>\d+)/$', OptionViewSet.as_view({
        'delete': 'destroy', 'get': 'retrieve', 'put': 'update'})),
    url(r'^goods/specs/simple/$', OptSpecView.as_view()),
    url(r'^skus/images/$', ImageViewSet.as_view({'get': 'list','post':'create'})),
    url(r'^skus/images/(?P<pk>\d+)/$', ImageViewSet.as_view({'get':'retrieve',
                                                             'put':'update','delete':'destroy'})),
    url(r'^skus/simple/$', SKUSimpleView.as_view()),
    url(r'^orders/$', OrderInfoView.as_view()),


]
router = SimpleRouter()
router.register(prefix='statistical', viewset=HomeView, base_name='home')
# # SPU
# router.register(prefix='goods',viewset=SPUViewSet,base_name='spu')
# # SPEC  发生路由屏蔽
# router.register(prefix='goods/specs',viewset=SpecViewSet,base_name='specs')
urlpatterns += router.urls
