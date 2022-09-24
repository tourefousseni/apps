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
      # path('upload/', views.image_upload_view, name='upload'),

      path('product/', views.product, name='product'),
      path('<int:product_id>/', views.product_detail, name='product_detail'),
      path('product_sum/', views.product_sum, name='product_sum'),

      # path('vuesimg/<int:upload_id>/', views.vuesimg, name='vues_img'),

      path('', views.user_login, name='login'),
      path('logout/', views.logout_user, name='logout'),
      path('register/', views.register_user, name='register'),
      path('profile/', views.profile, name='profile'),
      path('edit/profile/', views.edit_profile, name='edit_profile'),
      path('change/password/', views.change_password, name='change_password'),

      path('person/', views.person, name='person'),

      path('person/list/', views.list, name='list'),
      # path('person/list/<int:person_id>/', views.list, name='list'),
      path('person/detail/<int:p_detail_id>/', views.detail_person, name='detail_person'),
      # path('person/detail/<int:person_id>/', views.detail_person, name='detail_person'),

      path('user/', views.user, name='user'),

      path('n_customers/', views.n_customers, name='customer'),
      path('n_orders/', views.n_orders, name='order_count'),
      path('n_products/', views.n_products, name='product_count'),


      path('report_pdf/', views.report_pdf, name='report_pdf'),

      path('mesure/', views.mesure, name='mesure'),
      path('mesure_list/<int:mesure_id>/', views.mesure_list, name='mesure_list'),



      path('order/', views.order, name='order'),
      path('order_items/', views.order_items, name='order_items'),
      path('orderdetail/detail/<int:order_items_id>/', views.orderdetail_detail, name='orderdetail_detail'),
      path('order_list/<int:order_id>/', views.order_list, name='order_list'),

      path('show_video/', views.show_video, name='show_video'),


      path('payment/', views.payment, name='payment'),
      path('payment/list/<int:payment_id>/', views.payment_list, name='payment_list'),

     # PARTY MAPS LOCALISATION #
      path('maps/', views.maps, name='maps'),
      path('region/', views.region, name='region'),
      path('region/cercle/', views.cercle, name='cercle'),
      path('region/cercle/commune/', views.commune, name='commune'),
      path('region/cercle/commune/village/', views.village, name='village'),

      # GENERATED PDF
      path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
      path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),

    # Filter Person
      path('person_filter/', views.person_filter, name='person_filter'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# =================================
#         ULRS KALALISO
#             END
# =================================