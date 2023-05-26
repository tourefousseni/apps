from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'contacts'
# =================================
#         ULRS CONTACTS
#             STARTED
# =================================
urlpatterns = [

    path('person/', views.person, name='person'),
    path('list/', views.list, name='list'),
    path('person/<int:id>/', views.detail, name='detail'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('search_person/', views.search_person, name='search_person'),
    # path('person_paginator/', views.person_paginator, name='person_paginator'),
    path('report_card/<int:id>/', views.report_card, name="report_card"),
    path('report_all_person/', views.report_all_person, name="report_all_person"),

]
# =================================
#         ULRS CONTACTS
#             END
# =================================
