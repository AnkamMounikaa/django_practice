from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fav_item(req):
    return HttpResponse("Panner Butter Masala")

def fav_rest(req):
    return HttpResponse("Nayudu Gari Kunda Biryani")