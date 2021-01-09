from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls import url

# app_name = 'blog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
