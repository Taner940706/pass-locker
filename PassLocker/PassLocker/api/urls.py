from django.urls import path, include
from PassLocker.api.views import ListGroupApiView, CreateGroupApiView, EditGroupApiView, DeleteGroupApiView, \
    CreateLockerApiView, ListLockerApiView, EditLockerApiView, DeleteLockerApiView, ListUserApiView, CreateUserApiView, \
    EditUserApiView, DeleteUserApiView

urlpatterns = [
    path('groups/', ListGroupApiView.as_view(), name='list group api'),
    path('groups/create/', CreateGroupApiView.as_view(), name='create group api'),
    path('groups/<int:pk>/', include([
        path('edit/', EditGroupApiView.as_view(), name='edit group api'),
        path('delete/', DeleteGroupApiView.as_view(), name='delete group api'),
    ])),
    path('lockers/', ListLockerApiView.as_view(), name='list locker api'),
    path('lockers/create/', CreateLockerApiView.as_view(), name='create locker api'),
    path('lockers/<int:pk>/', include([
        path('edit/', EditLockerApiView.as_view(), name='edit locker api'),
        path('delete/', DeleteLockerApiView.as_view(), name='delete locker api'),
    ])),
    path('users/', ListUserApiView.as_view(), name='list user api'),
    path('users/create/', CreateUserApiView.as_view(), name='create locker api'),
    path('users/<int:pk>/', include([
        path('edit/', EditUserApiView.as_view(), name='edit locker api'),
        path('delete/', DeleteUserApiView.as_view(), name='delete user api'),
    ])),
]
