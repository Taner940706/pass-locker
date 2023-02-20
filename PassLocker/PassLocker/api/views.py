from rest_framework import generics as rest_views
from rest_framework.response import Response

from PassLocker.api.serializers import GroupModelSerializer, GroupModelCreateSerializer, GroupModelUpdateSerializer
from PassLocker.groups.models import GroupModel


# Create your views here.

class ListGroupApiView(rest_views.ListAPIView):
    queryset = GroupModel.objects.all()
    serializer_class = GroupModelSerializer


class CreateGroupApiView(rest_views.ListCreateAPIView):
    queryset = GroupModel.objects.all()
    serializer_class = GroupModelCreateSerializer

    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)


class EditGroupApiView(rest_views.RetrieveUpdateAPIView):
    queryset = GroupModel.objects.all()
    serializer_class = GroupModelUpdateSerializer
    lookup_field = "pk"





