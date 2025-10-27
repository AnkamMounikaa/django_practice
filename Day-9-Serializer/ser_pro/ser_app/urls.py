from django.urls import path 
from . import views

urlpatterns=[
    # path("update_user/<int:id>",view=views.update_user),
    path("delete_user/<int:id>",view=views.delete_user),
    path("get_users/",view=views.get_users),
    path("reg_user/",view=views.reg_user)
]