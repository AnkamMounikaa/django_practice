from django.shortcuts import render
from django.http import HttpResponse

def fav_movie(req):
    return HttpResponse("Salaar")

def fav_actor(rqu):
    return HttpResponse("Prabhass")