from django.contrib import admin
# from django.urls import path
from django.urls import include, path
from django.conf.urls import url
from contacts import views
# from blog import views
# from blog.views import post_detail, post_list
from django.conf import settings
from django.conf.urls.static import static


app_name = 'contacts'
           # 'authenticate',

urlpatterns = [
      # path('', admin.site.urls),
      # path('thanks/', views.thanks, name='thanks'),
      path('profil/', views.profil, name='profil'),
# =================================
#         ULRS CADASTRE
#             START
# =================================
      path('parcel/', views.parcel, name='parcel'),
      path('parcels/detail/<int:parcel_id>/', views.parcel_detail, name='parcel_detail'),
      path('contact/', views.contact, name='adresses'),
      path('contacts/detail/<int:contact_id>/', views.contact_detail, name='contact-detail'),
      path('', views.home, name='home'),
# =================================
#         ULRS CADASTRE
#             END
# =================================



# =================================
#         ULRS KALALISO
#             START
# =================================
#       url(r'^home/$', views.look, name='home'),
#       url(r'^index/$', views.indexpage, name='indexpage'),
#       # url(r'', views.indexpage, name='indexpage'),
#       # url(r'^newPage/$', views.newPage, name='newPage'),
#       url(r'^thanks/$', views.thanks, name='thanks'),
#       url(r'^getformdata/$', views.get_form_data, name='get-form-data'),
#       url(r'^getperson/$', views.list_person, name='list_personnes'),

      path('homepage/', views.homepage, name='homepage'),
      path('order/', views.order, name='order'),
      path('order/detail/<int:order_id>/', views.order_detail, name='order_detail'),
      path('product/', views.product, name='product'),
      path('product/detail/<int:product_id>/', views.product_detail, name='product_detail'),
      path('person/', views.person, name='person'),
      path('person/detail/<int:person_id>/', views.person_detail, name='person_detail'),
      path('payment/', views.payment, name='payment'),
      path('payment/detail/<int:payment_id>/', views.payment_detail, name='payment_detail'),
      path('mesure/', views.mesure, name='mesure'),
      path('mesure/detail/<int:mesure_id>/', views.mesure_detail, name='mesure_detail'),

# =================================
#         ULRS KALALISO
#             END
# =================================

      path('about/', views.about, name='about'),
      path('login/', views.user_login, name='login'),
      path('logout/', views.logout_user, name='logout'),
      path('register/', views.register_user, name='register'),
      path('edit/profile/', views.edit_profile, name='edit_profile'),
      path('change/password/', views.change_password, name='change_password'),
]
