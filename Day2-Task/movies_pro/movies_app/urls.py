from django.urls import path
from . import views 

urlpatterns=[
    path('fav_movie/',views.fav_movie),
    path('fav_actor/',views.fav_actor)
]