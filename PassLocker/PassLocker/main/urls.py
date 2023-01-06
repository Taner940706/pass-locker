from django.urls import path

from PassLocker.main.views import CreateLockerView, EditLockerView, DeleteLockerView

urlpatterns = (
    path('', CreateLockerView.as_view(), name='list locker'),
    path('create/', CreateLockerView.as_view(), name='create locker'),
    path('<int:pk>/edit/', EditLockerView.as_view(), name='edit locker'),
    path('<int:pk>/delete/', DeleteLockerView.as_view(), name='delete locker'),
)
