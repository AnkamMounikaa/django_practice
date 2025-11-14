from django.urls import path 
from . import views

urlpatterns=[
    path('msg/',view=views.msg),
    path('storage/',view=views.add_coder)
]