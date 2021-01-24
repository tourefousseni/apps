from django.contrib import admin
# from django.urls import path
from django.urls import include, path
from django.conf.urls import url
from blog import views
from contacts import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'blog', \
           'contacts',
# app_name = 'contacts',

urlpatterns = [
      path('', admin.site.urls),
      # path('posts', views.post_list, name='home'),
      # path('posts/<str:category_name>/', views.post_list, name='post-list'),
      # path('posts/detail/<int:post_id>/', views.post_detail, name='post-detail'),
      path('thanks/', views.thanks, name='thanks'),
      path('contact/', views.contact, name='adresses'),
      path('contacts/detail/<int:contact_id>/', views.contact_detail, name='contact-detail'),
]
 # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# post_list/