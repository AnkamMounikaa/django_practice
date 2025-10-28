from django.shortcuts import render
from .models import Student
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf  import csrf_exempt
import json
from .serializer import StudentSerializer
# Create your views here.
    
@csrf_exempt
def delete_user(req,id):
    try:
     existing_stu=Student.objects.get(stu_id=id)
     existing_stu.delete()
     return JsonResponse({"success":"user deleted!"})
    except:
        return HttpResponse("user not found!")


def get_users(req):
    all_data=Student.objects.all() 
    serialized_data=StudentSerializer(all_data,many=True)
    return JsonResponse({"data":serialized_data.data})


def reg_user(req):
    user_data=json.loads(req.body)    
    serialized_data=StudentSerializer(data=user_data,partial=True)
    if serialized_data.is_valid():
        serialized_data.save()
    return JsonResponse({"data":serialized_data.data})