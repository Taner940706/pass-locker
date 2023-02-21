from django.contrib.auth import get_user_model
from rest_framework import generics as rest_views


from PassLocker.api.serializers import GroupModelSerializer, GroupModelCreateSerializer, \
    LockerModelSerializer, AppUserModelSerializer, AppUserModelCreateSerializer, LockerModelCreateSerializer
from PassLocker.groups.models import GroupModel
from PassLocker.main.models import MainModel
UserModel = get_user_model()


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
    serializer_class = GroupModelSerializer
    lookup_field = "pk"


class DeleteGroupApiView(rest_views.RetrieveDestroyAPIView):
    queryset = GroupModel.objects.all()
    serializer_class = GroupModelSerializer
    lookup_field = "pk"


class ListLockerApiView(rest_views.ListAPIView):
    queryset = MainModel.objects.all()
    serializer_class = LockerModelSerializer


class CreateLockerApiView(rest_views.ListCreateAPIView):
    queryset = MainModel.objects.all()
    serializer_class = LockerModelCreateSerializer

    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)


class EditLockerApiView(rest_views.RetrieveUpdateAPIView):
    queryset = MainModel.objects.all()
    serializer_class = LockerModelSerializer
    lookup_field = "pk"


class DeleteLockerApiView(rest_views.RetrieveDestroyAPIView):
    queryset = MainModel.objects.all()
    serializer_class = LockerModelSerializer
    lookup_field = "pk"


class ListUserApiView(rest_views.ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = AppUserModelSerializer


class CreateUserApiView(rest_views.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = AppUserModelCreateSerializer

    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)


class EditUserApiView(rest_views.RetrieveUpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = AppUserModelSerializer
    lookup_field = "pk"


class DeleteUserApiView(rest_views.RetrieveDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = AppUserModelSerializer
    lookup_field = "pk"




