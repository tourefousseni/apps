from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
# from  . import views  program, genFooterTable, genBodyTable, genHeaderTable
from reportlab.platypus import Table
from accounts import views

from django.conf import settings
# from  reportlab.pdfgen views  genFooterTable, genBodyTable, genHeaderTable

app_name = 'accounts'

urlpatterns = [

      path('login/', views.login, name='login'),
      path('logout/', views.logout, name='logout'),
      path('register/', views.register, name='register'),
      path('dashboard/', views.dashboard, name='dashboard'),
      path('edit_profile/', views.edit_profile, name='edit_profile'),
      path('change_password/', views.change_password, name='change_password'),
]


      # path('upload/', views.image_upload_view, name='upload'),
      # path('vuesimg/<int:upload_id>/', views.vuesimg, name='vues_img'),

     # PATH FOR SEARCH CONTACTS OR NAME IN DATABASE
     #  path('search_person/', views.search_person, name='search_person'),

     #  path('person/list/search_person/', views.search_person, name='search_person'),
     #  path('person/list/person_paginator/', views.person_paginator, name='person_paginator'),

      # path('person/list/profile/', views.profile, name='profile'),
      #
      # path('edit/profile/', views.edit_profile, name='edit_profile'),
      # path('change/password/', views.change_password, name='change_password'),
      #
      # path('person/', views.person, name='person'),
      #
      # path('person/list/delete/<int:id>/', views.delete_person, name='delete_person'),
      #
      # path('person/list/', views.list, name='list'),
      # path('person/list/detail_person/<int:person_id>/', views.detail_person, name='detail_person'),
      # # path('person/list/delete_person/<int:person_id>/', views.delete_person, name='delete_person'),
      #
      # path('user/', views.user, name='user'),
      #
      # # GENERATED XHTML TO PDF
      # path('person/list/report-person-pdf/', views.report_person_pdf, name="report_person_pdf"),
      # path('person/list/report-person-id-pdf/<int:person_id>/', views.report_person_id_pdf, name="report_person_id_pdf"),
      # path('report_order/<int:order_id>/', views.report_order_pdf, name="report_order_pdf"),
      # path('report_mesure/', views.report_mesure_pdf, name="report_mesure_pdf"),

      # VIEWS PROFIL CUSTOMER
      # path('person/info_person/<int:id>/', views.info_person, name='info_person'),




# =================================
#         ULRS KALALISO
#             END
# =================================
