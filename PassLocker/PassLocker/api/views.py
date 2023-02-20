from rest_framework import generics as rest_views
from rest_framework.response import Response

from PassLocker.api.serializers import GroupModelSerializer, GroupModelCreateSerializer, GroupModelUpdateSerializer, \
    GroupModelDeleteSerializer, MainModelCreateSerializer, LockerModelSerializer, LockerModelUpdateSerializer, \
    LockerModelDeleteSerializer
from PassLocker.groups.models import GroupModel
from PassLocker.main.models import MainModel


# Create your views here.

class ListGroupApiView(rest_views.ListAPIView):
    queryset = GroupModel.objects.all()
    serializer_class = GroupModelSerializer


class ListLockerApiView(rest_views.ListAPIView):
    queryset = MainModel.objects.all()
    serializer_class = LockerModelSerializer


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


class EditLockerApiView(rest_views.RetrieveUpdateAPIView):
    queryset = MainModel.objects.all()
    serializer_class = LockerModelUpdateSerializer
    lookup_field = "pk"


class DeleteGroupApiView(rest_views.RetrieveDestroyAPIView):
    queryset = GroupModel.objects.all()
    serializer_class = GroupModelDeleteSerializer
    lookup_field = "pk"


class DeleteLockerApiView(rest_views.RetrieveDestroyAPIView):
    queryset = MainModel.objects.all()
    serializer_class = LockerModelDeleteSerializer
    lookup_field = "pk"


class CreateLockerApiView(rest_views.ListCreateAPIView):
    queryset = MainModel.objects.all()
    serializer_class = MainModelCreateSerializer

    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)