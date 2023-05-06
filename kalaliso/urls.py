from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from kalaliso import views
app_name = 'kalaliso'

urlpatterns = [

     path('mesure/', views.mesure, name='mesure'),
     path('list/', views.list, name='list'),
     path('report_mesure/', views.report_mesure, name='carnet_mesure'),
     path('detail/<int:id>/', views.detail, name='detail'),
     path('search/', views.search_mesure, name='search_mesure'),
     path('paginator_list_mesure/', views.paginator_list_mesure, name='paginator_list_mesure'),
     path('update/<int:id>/', views.update, name='update_mesure'),
     path('product/', views.product, name='product'),
     path('product/list', views.products_list, name='products_list'),
     path('show_video/', views.show_video, name='show_video'),
     path('albums/', views.album, name='album'),
     path('paypal-return/', views.paypal_return, name='paypal_return'),
     path('paypal-cancel/', views.paypal_cancel, name='paypal_cancel'),
     path('home/', views.home, name='home'),


    #   path('<int:product_id>/', views.product_detail, name='product_detail'),
    #   path('product_sum/', views.product_sum, name='product_sum'),
    #
    #   path('mesure/mesure_list/search_mesure/', views.search_mesure, name='search_mesure'),
    #   path('mesure_custom/<int:mesure_id>/', views.mesure_custom, name='mesure_custom'),

    #   path('order/', views.order, name='order'),
    #   path('order/order_list', views.order_list, name='order_list'),
    #   path('order_items/', views.order_items, name='order_items'),
    #   path('orderdetail/detail/<int:order_items_id>/', views.orderdetail_detail, name='orderdetail_detail'),
    #   path('order/order_list/<int:order_id>/', views.order_list, name='order_list'),

    #   path('payment/', views.payment, name='payment'),
    #   path('payment/list/<int:payment_id>/', views.payment_list, name='payment_list'),

]

# =================================
#         ULRS KALALISO
#             END
# =================================
