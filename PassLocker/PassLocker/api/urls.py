from django.urls import path

from PassLocker.api.views import ListGroupApiView, CreateGroupApiView, EditGroupApiView

urlpatterns = [
    path('groups/', ListGroupApiView.as_view(), name='list group api'),
    path('groups/create/', CreateGroupApiView.as_view(), name='create group api'),
    path('groups/edit/<int:pk>/', EditGroupApiView.as_view(), name='edit group api'),
]