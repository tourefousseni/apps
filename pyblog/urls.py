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
      path('profil/', views.profil, name='profil'),
      path('contact/', views.contact, name='adresses'),
      path('contacts/detail/<int:contact_id>/', views.contact_detail, name='contact-detail'),


]
 # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# post_list/


#
# urlpatterns = [
#      url(r'^admin/', admin.site.urls),
#      # url(r'', admin.site.urls),
#      url(r'^home/$', views.home, name='home'),
#      # url(r'^admin/$', views.home, name='home'),
#      url(r'^about/$', views.about, name='about'),
#      url(r'^login/$', views.user_login, name='login'),
#      url(r'^logout/$', views.logout_user, name='logout'),
#      url(r'^register/$', views.register_user, name='register'),
#      url(r'^edit/profile/$', views.edit_profile, name='edit_profile'),
#      url(r'^change/password/$', views.change_password, name='change_password'),
#      url(r'^products/', include('products.urls', namespace='products')),
# ]