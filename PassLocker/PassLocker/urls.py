from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import PassLocker.accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('PassLocker.accounts.urls')),
    path('locker/', include('PassLocker.main.urls')),
    path('group/', include('PassLocker.groups.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = PassLocker.accounts.views.Handler404.as_view()
handler500 = PassLocker.accounts.views.Handler500.as_view()
