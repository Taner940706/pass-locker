from django.urls import path

from PassLocker.groups.views import CreateGroupView, EditGroupView, DeleteGroupView, ListGroupView

urlpatterns = (
    path('', ListGroupView.as_view(), name='details group'),
    path('create/', CreateGroupView.as_view(), name='create group'),
    path('edit/<int:pk>/', EditGroupView.as_view(), name='edit group'),
    path('delete/<int:pk>/', DeleteGroupView.as_view(), name='delete group'),
)