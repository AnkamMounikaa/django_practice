from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Coders
@csrf_exempt
def add_coder(request):
    user_name=request.POST.get("username")
    user_age=request.POST.get("userage")
    
    coder = Coders.objects.create(name=user_name, age=user_age)
    coder.save()
    return JsonResponse({"message": "Coder added successfully!", "coder_id": coder.id})
    
    
