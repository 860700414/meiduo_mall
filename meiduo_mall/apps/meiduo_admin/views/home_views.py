#
# from rest_framework.viewsets import ViewSet
# from rest_framework.response import Response
# from rest_framework.decorators import action
# from django.conf import settings
#
# from orders.models import OrderInfo
# from users.models import User
# from datetime import timedelta
# from django.utils import timezone
#
# import pytz
#
# class HomeView(ViewSet):
#
#     @action(methods=['get'], detail=False)
#     def total_count(self, request):
#         # 1、计算用户数量和日期
#         count = User.objects.count()
#         date = timezone.now().date()
#         # 2、构建响应数据
#         return Response({
#             "count": count,
#             "date": date
#         })
#
#     @action(methods=['get'], detail=False)
#     def day_increment(self, request):
#         # 用户新建的日期，大于等于"当日"的"零点零分零秒"
#         # 就是当日新增
#
#         # 1、获取当日的零时: 上海的零时
#         # 时间类：年，月，日，时，分，秒，时区
#
#         # 2019-08-03 08:09:26.987697 +00:00
#         cur_date = timezone.now()
#
#         # 2019-08-03 16:09:26.987697 +08:00
#         shanghai_date = cur_date.astimezone(tz=pytz.timezone(settings.TIME_ZONE))
#
#         # 上海的零时
#         # 2019-08-03 00:00:00.000000 +08:00
#         shanghai_0_date = shanghai_date.replace(hour=0, minute=0, second=0, microsecond=0)
#
#         # 2、根据当日零时，过滤用户表
#         count = User.objects.filter(date_joined__gte=shanghai_0_date).count()
#
#         return Response({
#             "count": count,
#             "date": shanghai_0_date.date() # 2019-8-3
#         })
#
#     @action(methods=['get'], detail=False)
#     def day_active(self, request):
#         # 1、获取当日零点
#         local_0_time = timezone.now().astimezone(tz=pytz.timezone(settings.TIME_ZONE))\
#             .replace(hour=0, minute=0, second=0, microsecond=0)
#
#         # 2、过滤最后登陆日期大于等于当日零点
#         count = User.objects.filter(last_login__gte=local_0_time).count()
#
#         # 3、返回
#         return Response({
#             "count": count,
#             "date": local_0_time.date()
#         })
#
#     @action(methods=['get'], detail=False)
#     def day_orders(self, request):
#         # 统计今天下单的用户数量
#         # 已知条件：今天的零点（订单的创建时间） --> 从表的已知条件
#         # 目标数据：用户数量 --> 主表数据
#
#         # 1、统计出今天下的订单
#         local_0_time = timezone.now().astimezone(tz=pytz.timezone(settings.TIME_ZONE))\
#             .replace(hour=0, minute=0, second=0, microsecond=0)
#
#         # 从从表入手
#         # 2.1、找出今天下的所有订单
#         # order_queryset = OrderInfo.objects.filter(create_time__gte=local_0_time)
#         # 2.2 取出每个从表对象关联的主表，并统计主表数据
#         # user_list = []
#         # for order in order_queryset:
#             # order是单一的订单对象
#             # user_list.append(order.user)
#         # count = len(set(user_list))
#
#         # 从主表入手
#         user_queryset = User.objects.filter(orders__create_time__gte=local_0_time)
#         count = len(set(user_queryset))
#
#         # 3、返回
#         return Response({
#             "count": count,
#             "date": local_0_time.date()
#         })
#
#     @action(methods=['get'], detail=False)
#     def month_increment(self, request):
#         # 统计最近30天，每一天新增用户
#         # 1、当天的时间点
#         # 2019-8-3 0:0:0
#         cur_0_time = timezone.now().astimezone(pytz.timezone(settings.TIME_ZONE))\
#             .replace(hour=0, second=0, minute=0, microsecond=0)
#         # 2、起始时间点
#         # 起始时间点 = 当天的时间点 - （统计天数 - 一天）
#         begin_0_time = cur_0_time - timedelta(days=29)
#
#         calc_list = []
#         for index in range(30):
#             # calc_0_time：30天中的某一天
#             calc_0_time = begin_0_time + timedelta(days=index)
#
#             count = User.objects.filter(date_joined__gte=calc_0_time,
#                                         date_joined__lt=calc_0_time+timedelta(days=1)).count()
#
#
#             calc_list.append({
#                 "count": count,
#                 "date": calc_0_time.date()
#             })
#
#         return Response(calc_list)
#
#
#
#
#
from datetime import timedelta

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser, AllowAny
from users.models import User
from orders.models import OrderInfo

from django.utils import timezone
from django.conf import settings
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from meiduo_admin.serializers.home_serializer import *
import pytz


# class HomeView(ViewSet):
#     permission_classes = [IsAdminUser]
#
#     @action(methods=['get'], detail=False)
#     def total_count(self, request):
#         count = User.objects.count()
#         date = timezone.now().date()
#         return Response({'count': count, 'date': 'date'})
#
#     @action(methods=['get'], detail=False)
#     def day_incrementd(self, request):
#         cur_date = timezone.now()
#         shanghai_0_time = cur_date.astimezone(tz=pytz.timezone(settings.TIME_ZONE)).replace(hour=0, minute=0, second=0,
#                                                                                             microsecond=0)
#         count = User.objects.filter(date_joined__gte=shanghai_0_time).count()
#         return Response({'count': count, 'date': shanghai_0_time.date()})
#
#     def day_active(self, request):
#         local_0_date = timezone.now().astimezone(tz=pytz.timezone(settings.TIME_ZONE)).replace(hour=0, minute=0,
#                                                                                                second=0, microsecond=0)
#         count = User.objects.filter(last_login__gte=local_0_date).count()
#         return Response({'count': count, 'date': local_0_date.date()})
#
#     @action(methods=['get'], detail=False)
#     def day_orders(self, request):
#         local_0_time = timezone.now().astimezone(tz=pytz.timezone(settings.TIME_ZONE)).replace(hour=0, minute=0,
#                                                                                                second=0, microsecond=0)
#         # order_queryset=OrderInfo.objects.filter(create_time__gte=local_0_time)
#         user_queryset = User.objects.filter(orders__create_time__gte=local_0_time)
#         count = len(set(user_queryset))
#         return Response({'count': count, 'date': local_0_time.date()})
#
#     @action(methods=['get'], detail=False)
#     def month_increment(self, request):
#         currentotime = timezone.now().astimezone(tz=pytz.timezone(settings.TIME_ZONE)).replace(hour=0, minute=0,
#                                                                                                second=0, microsecond=0)
#         beginotine = currentotime - timedelta(days=29)
#         cal_list = []
#         for index in range(30):
#             calOtime = beginotine + timedelta(days=index)
#             count = User.objects.filter(date_joined__gte=calOtime, date_joined__lt=calOtime + timedelta(days=1)).count()
#             cal_list.append({'count': count, 'date': calOtime.date()})
#             return Response(cal_list)
#
# class GoodsVisitCountView(ListAPIView):
#     permission_classes = [IsAdminUser]
#     queryset = GoodsVisitCount.objects.all()
#     serializer_class = GoodsVisitCountSerializer
#
#     def get_queryset(self):
#         curotime = timezone.now().astimezone(pytz.timezone(settings.TIME_ZONE)).replace(hour=0, minute=0, second=0, microsecond=0)
#         return self.queryset.filter(create_time__gte=curotime)


class HomeView(ViewSet):
    permission_classes = [IsAdminUser]

    # 重写函数，实现特定接口权限管理
    # def get_permissions(self):
    # #     total_count  IsAdminUser
    #     if self.action=='total_count':
    #         return [IsAdminUser()]
    #     else:
    #         return [AllowAny()]
    @action(methods=['get'], detail=False)
    def total_count(self, request):
        count = User.objects.count()
        date = timezone.now().date()
        return Response({
            "count": count,
            "date": date
        })

    @action(methods=['get'], detail=False)
    def day_increment(self, request):
        cur_date = timezone.now()
        shanghai_date = cur_date.astimezone(tz=pytz.timezone(settings.TIME_ZONE))
        shanghai_0_date = shanghai_date.replace(hour=0, minute=0, second=0, microsecond=0)
        count = User.objects.filter(date_joined__gte=shanghai_0_date).count()

        return Response({
            'count': count,
            'date': shanghai_0_date.date()
        })

    @action(methods=['get'], detail=False)
    def day_active(self, request):
        local_0_date = timezone.now().astimezone(tz=pytz.timezone(settings.TIME_ZONE)) \
            .replace(hour=0, minute=0, second=0, microsecond=0)
        count = User.objects.filter(last_login__gte=local_0_date).count()
        return Response({
            'count': count,
            'date': local_0_date.date()
        })

    @action(methods=['get'], detail=False)
    def day_orders(self, request):
        # 已知条件，今天零点，，目标数据：用户数量是主表数据
        local_0_time = timezone.now().astimezone(tz=pytz.timezone(settings.TIME_ZONE)).replace(hour=0, minute=0,
                                                                                               second=0, microsecond=0)
        # order_queryset = OrderInfo.objects.filter(create_time__gte=local_0_time)
        # user_list=[]
        # for order in order_queryset:
        #     user_list.append(order.user)
        # count=len(set(user_list))
        user_queryset = User.objects.filter(orders__create_time__gte=local_0_time)
        count = len(set(user_queryset))
        return Response({
            'count': count,
            'date': local_0_time.date()
        })

    @action(methods=['get'], detail=False)
    def month_increment(self, request):
        #         dangtian
        cur_0_time = timezone.now().astimezone(pytz.timezone(settings.TIME_ZONE)).replace(hour=0, minute=0, second=0,
                                                                                          microsecond=0)

        begin_0_time = cur_0_time - timedelta(days=29)
        calc_list = []
        for index in range(30):
            calc_0_time = begin_0_time + timedelta(days=index)
            count = User.objects.filter(date_joined__gte=calc_0_time,
                                        date_joined__lt=calc_0_time + timedelta(days=1)).count()
            calc_list.append({
                'count': count,
                'date': calc_0_time.date()
            })
        return Response(calc_list)

class GoodsVisitCountView(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = GoodsVisitCount.objects.all()
    serializer_class = GoodsVisitCountSerializer
    def get_queryset(self):
        cur_0_time = timezone.now().astimezone(pytz.timezone(settings.TIME_ZONE)).replace(hour=0, minute=0, second=0, microsecond=0)
        return self.queryset.filter(create_time__gte=cur_0_time)
