from django.contrib import admin
from django.urls import path, include

app_name = 'contacts'

urlpatterns = [
      path('admin/', admin.site.urls),
      path('contacts/', include('contacts.urls', namespace='contacts')),
]
