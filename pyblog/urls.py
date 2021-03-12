from django.contrib import admin
# from django.urls import path
from django.urls import include, path
from django.conf.urls import url
from  contacts import views
# from  .import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'contacts',
           # 'blog', \
           # 'authenticate',

urlpatterns = [
      path('', admin.site.urls),
      # path('posts', views.post_list, name='home'),
      # path('posts/<str:category_name>/', views.post_list, name='post-list'),
      # path('posts/detail/<int:post_id>/', views.post_detail, name='post-detail'),

      # path('thanks/', views.thanks, name='thanks'),
      path('profil/', views.profil, name='profil'),
      path('contact/', views.contact, name='adresses'),
      path('contacts/detail/<int:contact_id>/', views.contact_detail, name='contact-detail'),

      path('home/', views.home, name='home'),
      path('about/', views.about, name='about'),
      path('login/', views.user_login, name='login'),
      path('logout/', views.logout_user, name='logout'),
      path('register/', views.register_user, name='register'),
      path('edit/profile/', views.edit_profile, name='edit_profile'),
      path('change/password/', views.change_password, name='change_password'),
]
