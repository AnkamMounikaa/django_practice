from django.urls import path 
from . import views

urlpatterns=[
    path("get_users/",view=views.get_user),
    path("reg_users/",view=views.reg_user),
    path("update_users/",view=views.update_user)
    
]