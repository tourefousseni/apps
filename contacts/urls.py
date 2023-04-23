from django.contrib import admin
from django.urls import include, path
from contacts import views

app_name = 'contacts'


# =================================
#         ULRS CONTACTS
#             STARTED
# =================================
urlpatterns = [

    path('person/', views.person, name='person'),
    path('person/list/', views.list, name='list'),
    # path('person/<int:id>/', views.detail, name='detail'),
    path('search/', views.search, name='search'),
    path('report_card/<int:id>/', views.report_card, name="report_card"),
    path('delete/<int:id>/', views.delete, name="delete"),
]
# =================================
#         ULRS CONTACTS
#             END
# =================================
