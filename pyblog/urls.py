from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
# from  contacts import views
# from  . import views  program, genFooterTable, genBodyTable, genHeaderTable
from reportlab.platypus import Table
from contacts import views
# from  reportlab.pdfgen views  genFooterTable, genBodyTable, genHeaderTable

app_name = 'contacts'

urlpatterns = (

      # path('home/', views.HomePageView, name='homepage'),
      # path('home/', HomePageView.as_view(), name='homepage'),
      path('homepage/', views.homepage, name='add_post'),
      path('upload/', views.image_upload_view, name='upload'),
      # path('', views.homepage, name='add_post'),

      # path('post/', views.createpost, name='add_post'),
      # path('post', CreatePostView.as_view(), name='add_post'),


      path('login/', views.user_login, name='login'),
      path('logout/', views.logout_user, name='logout'),
      path('register/', views.register_user, name='register'),
      path('profile/', views.profile, name='profile'),
      path('edit/profile/', views.edit_profile, name='edit_profile'),
      path('change/password/', views.change_password, name='change_password'),
      path('orderdetail/', views.orderdetail, name='orderdetail'),
      path('orderdetail/detail/<int:orderdetail_id>/', views.orderdetail_detail, name='orderdetail_detail'),
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
      path('region/', views.region, name='region'), path('cercle/', views.cercle, name='cercle'),
      path('arrondissement/', views.arrondissement, name='arrondissement'),
      path('commune/', views.commune, name='commune'), path('village/', views.village, name='village'),

)

# =================================
#         ULRS KALALISO
#             END
# =================================