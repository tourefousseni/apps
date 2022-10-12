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
      path('', views.homepage, name='homepage'),
      # path('upload/', views.image_upload_view, name='upload'),

      path('product/', views.product, name='product'),
      path('product/products_list', views.products_list, name='products_list'),
      path('<int:product_id>/', views.product_detail, name='product_detail'),
      path('product_sum/', views.product_sum, name='product_sum'),

      # path('vuesimg/<int:upload_id>/', views.vuesimg, name='vues_img'),

     # PATH FOR SEARCH CONTACTS OR NAME IN DATABASE
     #  path('search_person/', views.search_person, name='search_person'),
      path('person/list/search_person/', views.search_person, name='search_person'),
      path('person/list/person_paginator/', views.person_paginator, name='person_paginator'),


      path('', views.user_login, name='login'),
      path('logout/', views.logout_user, name='logout'),
      path('register/', views.register_user, name='register'),

      path('person/list/profile/', views.profile, name='profile'),

      path('edit/profile/', views.edit_profile, name='edit_profile'),
      path('change/password/', views.change_password, name='change_password'),

      path('person/', views.person, name='person'),
      path('person/list/', views.list, name='list'),
      path('detail_person/<int:person_id>/', views.detail_person, name='detail_person'),

      path('user/', views.user, name='user'),

      path('n_customers/', views.n_customers, name='customer'),
      path('n_orders/', views.n_orders, name='order_count'),
      path('n_products/', views.n_products, name='product_count'),

      path('mesure/', views.mesure, name='mesure'),
      path('mesure/mesure_list/', views.mesure_list, name='mesure_list'),
      path('mesure/mesure_list/search_mesure/', views.search_mesure, name='search_mesure'),
      path('mesure_custom/<int:mesure_id>/', views.mesure_custom, name='mesure_custom'),

      path('order/', views.order, name='order'),
      path('order/order_list', views.order_list, name='order_list'),
      path('order_items/', views.order_items, name='order_items'),
      path('orderdetail/detail/<int:order_items_id>/', views.orderdetail_detail, name='orderdetail_detail'),
      # path('order/order_list/<int:order_id>/', views.order_list, name='order_list'),

      path('show_video/', views.show_video, name='show_video'),

      path('payment/', views.payment, name='payment'),
      path('payment/list/<int:payment_id>/', views.payment_list, name='payment_list'),

     # PARTY MAPS LOCALISATION #
      path('maps/', views.maps, name='maps'),
      path('region/', views.region, name='region'),
      path('region/cercle/', views.cercle, name='cercle'),
      path('region/cercle/commune/', views.commune, name='commune'),
      path('region/cercle/commune/village/', views.village, name='village'),

      # GENERATED XHTML TO PDF
      path('person/list/report-person-pdf/', views.report_person_pdf, name="report_person_pdf"),
      path('person/list/report-person-id-pdf/<int:person_id>/', views.report_person_id_pdf, name="report_person_id_pdf"),
      path('report_order/<int:order_id>/', views.report_order_pdf, name="report_order_pdf"),
      path('report_mesure/', views.report_mesure_pdf, name="report_mesure_pdf"),

      # VIEWS PROFIL CUSTOMER
      # path('person/info_person/<int:id>/', views.info_person, name='info_person'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# =================================
#         ULRS KALALISO
#             END
# =================================