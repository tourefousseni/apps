from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
# from  .import views
# from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static
app_name = 'contacts'

urlpatterns = [
      path('admin/', admin.site.urls),
      path('contacts/', include('contacts.urls', namespace='contacts')),
]
if settings.DEBUG:
      urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# =================================
#         ULRS KALALISO
#             START
# =================================