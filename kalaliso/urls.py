from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
# from  . import views  program, genFooterTable, genBodyTable, genHeaderTable
from reportlab.platypus import Table
from kalaliso import views
# from  reportlab.pdfgen views  genFooterTable, genBodyTable, genHeaderTable

app_name = 'kalaliso'

urlpatterns = [

    # path('product/', views.product, name='product'),
    # path('product/products_list', views.products_list, name='products_list'),
    # path('<int:product_id>/', views.product_detail, name='product_detail'),
    # path('product_sum/', views.product_sum, name='product_sum'),
     path('mesure/', views.mesure, name='mesure'),
    #
    #   path('mesure/mesure_list/<int:id>/', views.mesure_detail, name='mesure_detail'),
      path('list/', views.list, name='list'),
      path('report_mesure/', views.report_mesure, name='report_mesure'),
    #   path('mesure/mesure_list/search_mesure/', views.search_mesure, name='search_mesure'),
    #   # path('mesure_custom/<int:mesure_id>/', views.mesure_custom, name='mesure_custom'),
    #
    #   path('order/', views.order, name='order'),
    #   path('order/order_list', views.order_list, name='order_list'),
    #   path('order_items/', views.order_items, name='order_items'),
    #   path('orderdetail/detail/<int:order_items_id>/', views.orderdetail_detail, name='orderdetail_detail'),
    #   # path('order/order_list/<int:order_id>/', views.order_list, name='order_list'),
    #
    #   path('show_video/', views.show_video, name='show_video'),
    #
    #   path('payment/', views.payment, name='payment'),
    #   path('payment/list/<int:payment_id>/', views.payment_list, name='payment_list'),

]

# =================================
#         ULRS KALALISO
#             END
# =================================
