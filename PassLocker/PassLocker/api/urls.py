from django.urls import path

from PassLocker.api.serializers import LockerModelUpdateSerializer
from PassLocker.api.views import ListGroupApiView, CreateGroupApiView, EditGroupApiView, DeleteGroupApiView, \
    CreateLockerApiView, ListLockerApiView, EditLockerApiView, DeleteLockerApiView

urlpatterns = [
    path('groups/', ListGroupApiView.as_view(), name='list group api'),
    path('lockers/', ListLockerApiView.as_view(), name='list locker api'),
    path('groups/create/', CreateGroupApiView.as_view(), name='create group api'),
    path('groups/edit/<int:pk>/', EditGroupApiView.as_view(), name='edit group api'),
    path('lockers/edit/<int:pk>/', EditLockerApiView.as_view(), name='edit locker api'),
    path('groups/delete/<int:pk>/', DeleteGroupApiView.as_view(), name='delete group api'),
    path('lockers/delete/<int:pk>/', DeleteLockerApiView.as_view(), name='delete locker api'),
    path('lockers/create/', CreateLockerApiView.as_view(), name='create locker api'),
]