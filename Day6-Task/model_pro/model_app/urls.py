from django.urls import path 
from . import views

urlpatterns=[
    path('storage/',view=views.add_coder)
]