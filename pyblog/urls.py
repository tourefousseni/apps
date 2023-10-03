from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
      path('', include('pages.urls',)),
      path('maps/', include('maps.urls',)),
      path('contacts/', include('contacts.urls',)),
      path('accounts/',include('accounts.urls',)),
      path('kalaliso/', include('kalaliso.urls',)),
      path('paypal/', include('paypal.standard.ipn.urls')),
      path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
