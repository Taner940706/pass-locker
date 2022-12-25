from django.urls import path

from PassLocker.main.views import CreateLockerView, EditLockerView, DeleteLockerView

urlpatterns = (
    path('create/', CreateLockerView.as_view(), name='add locker'),
    path('edit/<int:pk>/', EditLockerView.as_view(), name='edit locker'),
    path('delete/<int:pk>/', DeleteLockerView.as_view(), name='delete locker'),
)
