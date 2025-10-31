from django.urls import path 
from . import views

urlpatterns=[
    path("post_m/",view=views.post_method),
    # path("patch_m/",view=views.patch_method),
    # path("put_m/",view=views.put_method),
    #  path("delete_m/",view=views.delete_method)
]