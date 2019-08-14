from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import Permission, ContentType

from meiduo_admin.pages import MyPage
from meiduo_admin.serializers.perms_serializer import PermSerializer, ContentTypeSerializser
from rest_framework.decorators import action
from rest_framework.response import Response


class PermViewSet(ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermSerializer
    pagination_class = MyPage

    def get_queryset(self):
        if self.action == 'content_types':
            return ContentType.objects.all()
        return self.queryset.all()

    def get_serializer_class(self):
        if self.action == 'content_types':
            return ContentTypeSerializser
        return self.serializer_class

    """
           Return the class to use for the serializer.
           Defaults to using `self.serializer_class`.

           You may want to override this if you need to provide different
           serializations depending on the incoming request.

           (Eg. admins get full serialization, others get basic serialization)
    """

    @action(methods=['get'], detail=False)
    def content_types(self, request):
        content_typeset = self.get_queryset()
        serializer = self.get_serializer(content_typeset, many=True)
        return Response(serializer.data)
