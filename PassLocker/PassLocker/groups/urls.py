from django.urls import path

from PassLocker.groups.views import CreateGroupView, EditGroupView, DeleteGroupView, ListGroupView

urlpatterns = (
    path('', ListGroupView.as_view(), name='details group'),
    path('create/', CreateGroupView.as_view(), name='create group'),
    path('<int:pk>/edit/', EditGroupView.as_view(), name='edit group'),
    path('<int:pk>/delete/', DeleteGroupView.as_view(), name='delete group'),
)