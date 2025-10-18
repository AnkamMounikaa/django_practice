from django.urls import path 
from .import views
urlpatterns=[
    path('get_details/', view=views.get_details),
    path('details/',view=views.stu_details)
    
]