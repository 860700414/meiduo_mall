from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class MyPage(PageNumberPagination):
    page_query_param = 'page'
    max_page_size = 10
    page_size_query_param = 'pagesize'


    def get_paginated_response(self, data):
        """
        构建相应对象 返回对象数据
        :param data:
        :return:
        """

        return Response({
            'counts':self.page.paginator.count,
            'lists':data,
            'page':self.page.number,
            'pages':self.page.paginator.num_pages,
            'pagesize':self.page_size,
        })

