from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

# app_name = 'blog'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('contacts.urls')),
]
