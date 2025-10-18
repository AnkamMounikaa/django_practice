from django.urls import path
from . import views 

urlpatterns=[
    path('favFood/', views.fav_item),
    path('favRes/',views.fav_rest)
]