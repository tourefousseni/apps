from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from .views import home, about,\
     user_login, logout_user, edit_profile, \
     change_password, register_user, \
     render, redirect

app_name = 'accounts'

urlpatterns = [
    # path('admin/', admin.site.urls),

    path(r'home/', views.home, name='home'),
    # url(r'^admin/$', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('edit/profile/', views.edit_profile, name='edit_profile'),
    path('change/password/', views.change_password, name='change_password'),
    path('', include('accounts.urls')),
]
