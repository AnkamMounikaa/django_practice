from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.

def reg_user(req):
    return HttpResponse("reg is working")