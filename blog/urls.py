from django.contrib import admin
from django.urls import include, path
from .import views

app_name = 'blog'
# =================================
#         ULRS BLOG
#             STARTED
# =================================
urlpatterns = [

    path('annonce/', views.annonce, name='annonce'),
    path('annonce/<int:id>/', views.detail_annonce, name='detail_annonce'),
    # path('update/<int:id>/', views.update, name='update'),
    # path('delete/<int:id>/', views.delete, name="delete"),
    # path('search_person/', views.search_person, name='search_person'),
    # path('person_paginator/', views.person_paginator, name='person_paginator'),

]
# =================================
#         ULRS BLOG
#             END
# =================================
