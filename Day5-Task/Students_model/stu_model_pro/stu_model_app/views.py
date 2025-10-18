from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Stundent_details


def get_details(request):
    if request.method=="GET":
        user=Stundent_details.objects.all()
        data=list(user.values())
        return JsonResponse({"data":list(data)})

@csrf_exempt
def stu_details(request):
    if request.method=="POST":
        user_fname=request.POST.get("userfname")
        user_lname=request.POST.get("userlname")
        user_age=request.POST.get("userage")
        user_rollnum=request.POST.get("userrollnum")

        details = Stundent_details.objects.create(first_name=user_fname,last_name=user_lname, age=user_age, roll_num=user_rollnum)
        details.save()
        return JsonResponse({"message": "Coder added successfully!", "coder_id": details.id})