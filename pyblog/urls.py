from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
# from  contacts import views
# from  . import views  program, genFooterTable, genBodyTable, genHeaderTable
from reportlab.platypus import Table
from contacts import views
# from  reportlab.pdfgen views  genFooterTable, genBodyTable, genHeaderTable

app_name = 'contacts'

urlpatterns = [

      # path('home/', views.HomePageView, name='homepage'),
      # path('home/', HomePageView.as_view(), name='homepage'),
      path('admin/', admin.site.urls),
      path('', views.homepage, name='homepage'),
      path('upload/', views.image_upload_view, name='upload'),
      path('vuesimg/<int:upload_id>/', views.vuesimg, name='vues_img'),

      # path('(?P<id>[0-9]+)/upload_detaitl/$', views.upload_detail, name='upload_detail'),
      # path('upload_detail/<int:id>/', views.upload_detail, name='upload_detail'),
      # path('upload/<int:id>/', views.image_upload_view_detail, name='upload-detail'),
      # path('product/<int:id>/', views.product_detail, name='product-detail'),
      # path('', views.homepage, name='add_post'),

      path('login/', views.user_login, name='login'),
      path('logout/', views.logout_user, name='logout'),
      path('register/', views.register_user, name='register'),
      path('profile/', views.profile, name='profile'),
      path('edit/profile/', views.edit_profile, name='edit_profile'),
      path('change/password/', views.change_password, name='change_password'),

      path('orderdetail/detail/<int:order_items_id>/', views.orderdetail_detail, name='orderdetail_detail'),
      path('order/', views.order, name='order'),
      path('order_items/', views.order_items, name='order_items'),
      path('order/detail/<int:order_id>/', views.order_items, name='order_items'),
      path('product/', views.product, name='product'),
      path('product/detail/<int:product_id>/', views.product_detail, name='product_detail'),

      path('person/', views.person, name='person'),
      path('person/detail/<int:person_id>/', views.person_detail, name='person_detail'),


      path('payment/', views.payment, name='payment'),
      path('payment/detail/<int:payment_id>/', views.payment_detail, name='payment_detail'),
      path('mesure/', views.mesure, name='mesure'),
      path('mesure/detail/<int:mesure_id>/', views.mesure_detail, name='mesure_detail'),

     # PARTY MAPS LOCALISATION #
      path('maps/', views.maps, name='maps'),
      path('region/', views.region, name='region'),
      path('region/cercle/', views.cercle, name='cercle'),
      path('region/cercle/commune/', views.commune, name='commune'),
      path('region/cercle/commune/village/', views.village, name='village'),
]


# =================================
#         ULRS KALALISO
#             END
# =================================