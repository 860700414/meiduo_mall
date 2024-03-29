from django.contrib.auth.backends import ModelBackend
from django.http import HttpRequest
import re
from users.models import User
from django.utils import timezone

class MeiduoModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        自定义认证流程
        :param request: 请求对象
        :param username: 用户名
        :param password: 密码
        :param kwargs: 额外参数
        :return: 返回None表示认证失败，返回User对象表明认证成功(对应的权限：IsAuthentication)
        """

        try:

            user = User.objects.get(username=username)
        except:
            # 如果未查到数据，则返回None，用于后续判断
            try:
                user = User.objects.get(mobile=username)
            except:
                return None

        # 后台管理站点登陆  的时候，不会传入request,设置isstaff为0
        if not request and not user.is_staff:
            return None


        # 判断密码
        if user.check_password(password):
            return user
        else:
            return None

