from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
# from  . import views  program, genFooterTable, genBodyTable, genHeaderTable
from reportlab.platypus import Table
from contacts import views
from django.conf import settings
from django.conf.urls.static import static
# from  reportlab.pdfgen views  genFooterTable, genBodyTable, genHeaderTable

app_name = 'contacts'

urlpatterns = [

      path('admin/', admin.site.urls),
      path('homepage/', views.homepage, name='homepage'),
      path('upload/', views.image_upload_view, name='upload'),
      path('vuesimg/<int:upload_id>/', views.vuesimg, name='vues_img'),

      path('', views.user_login, name='login'),
      path('logout/', views.logout_user, name='logout'),
      path('register/', views.register_user, name='register'),
      path('profile/', views.profile, name='profile'),
      path('edit/profile/', views.edit_profile, name='edit_profile'),
      path('change/password/', views.change_password, name='change_password'),

      path('person/', views.person, name='person'),
      path('person/<int:person_id>/', views.person_list, name='person_list'),

      path('order/', views.order, name='order'), path('order_items/', views.order_items, name='order_items'),
      path('order/list/<int:order_id>/', views.order_list, name='order_list'),

      path('mesure/', views.mesure, name='mesure'),
      path('mesure/list/<int:mesure_id>/', views.mesure_list, name='mesure_list'),

      path('product/', views.product, name='product'),
      path('product/list/<int:product_id>/', views.product_list, name='product_list'),

      path('payment/', views.payment, name='payment'),
      path('payment/list/<int:payment_id>/', views.payment_list, name='payment_list'),

     # PARTY MAPS LOCALISATION #
      path('maps/', views.maps, name='maps'),
      path('region/', views.region, name='region'),
      path('region/cercle/', views.cercle, name='cercle'),
      path('region/cercle/commune/', views.commune, name='commune'),
      path('region/cercle/commune/village/', views.village, name='village'),

      path('orderdetail/detail/<int:order_items_id>/', views.orderdetail_detail, name='orderdetail_detail'),
]
if settings.DEBUG:
      urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# =================================
#         ULRS KALALISO
#             END
# =================================