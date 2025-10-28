from django.urls import path 
from . import views
urlpatterns=[
    path("delete_user/<int:id>",view=views.delete_user),
    path("get_users/",view=views.get_users),
    path("reg_user/",view=views.reg_user)
]