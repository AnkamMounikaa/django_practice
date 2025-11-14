from django.urls import path 
from . import views

urlpatterns=[
    path("reg_user/",view=views.reg_user),
    path("get_users/",view=views.get_users),
    path("delete_user/<int:id>",view=views.delete_user)
    
]