from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from blog import views
# from django.conf import settings
# from django.conf.urls.static import static


app_name = 'blog'

urlpatterns = [
      path('', admin.site.urls),
      path('post_list/', views.post_list, name='home'),
      path('posts/<str:category_name>/', views.post_list, name='post-list'),
      path('posts/detail/<int:post_id>/', views.post_detail, name='post-detail'),
]
 # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
