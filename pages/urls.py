from django.urls import path
from . import views

namespace = 'pages'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.about, name='about'),
]