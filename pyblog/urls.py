from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from contacts import views
# from  . import views  program, genFooterTable, genBodyTable, genHeaderTable
from reportlab.platypus import Table
# from  .import views
# from  reportlab.pdfgen views  genFooterTable, genBodyTable, genHeaderTable
from django.conf import settings
from django.conf.urls.static import static


app_name = 'contacts'
           # 'authenticate',

urlpatterns = [
      path('', admin.site.urls),
      # path('thanks/', views.thanks, name='thanks'),

      # =================================
      #         ULRS INVOICE
      #             START
      # =================================
      # path('fiche/', views.fiche, name='fiche'),
      # path('header/', views.genHeaderTable, name='header'),
      # path('body/', views.genBodyTable, name='body'),
      # path('footer/', views.genFooterTable, name='footer'),
      path('program/', views.program, name='program'),
      # =================================
      #         ULRS INVOICE
      #             START
      # =================================

      # =================================
      #         ULRS CADASTRE
      #             START
      # =================================

      path('profil_pdf/', views.profil_pdf, name='profil_pdf'),
      path('parcel/', views.parcel, name='parcel'),
      path('parcels/detail/<int:parcel_id>/', views.parcel_detail, name='parcel_detail'),
      path('contact/', views.contact, name='adresses'),
      path('contact/detail/<int:contact_id>/', views.contact_detail, name='contact-detail'),
      path('', views.home, name='home'),
      # =================================
      #         ULRS CADASTRE
      #             END
      # =================================

      # =================================
      #         ULRS KALALISO
      #             START
      # =================================
      path('homepage/', views.homepage, name='homepage'),
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

      # =================================
      #         ULRS KALALISO
      #             END
      # =================================

      # =================================
      #         ULRS LOGIN
      #             START
      # =================================
      path('about/', views.about, name='about'),
      path('login/', views.user_login, name='login'),
      path('logout/', views.logout_user, name='logout'),
      path('register/', views.register_user, name='register'),
      path('edit/profile/', views.edit_profile, name='edit_profile'),
      path('change/password/', views.change_password, name='change_password'),
      # =================================
      #         ULRS LOGIN
      #             END
      # =================================
]
