from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from accounts import views
from django.conf import settings

app_name = 'accounts'

# =================================
#         ULRS ACCOUNTS
#             START
# =================================
urlpatterns = [

      path('', views.login, name='login'),
      path('logout/', views.logout, name='logout'),
      path('register/', views.register, name='register'),
      path('dashboard/', views.dashboard, name='dashboard'),
      path('edit_profile/', views.edit_profile, name='edit_profile'),
      path('change_password/', views.change_password, name='change_password'),
]
# =================================
#         ULRS ACCOUNTS
#             END
# =================================
