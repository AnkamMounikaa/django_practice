from django.shortcuts import render
from .models import Student
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf  import csrf_exempt
import json
from .serializer import StudentSerializer
# Create your views here.

# @csrf_exempt
# def update_user(req,id):
#     user_data=json.loads(req.body)
#     print(user_data["stu_branch"])
    
#     try:
#      stu_exists=Student.objects.get(stu_id=id) #
#      stu_exists=list(stu_exists)[0]
#      print(stu_exists)
    
#      if stu_exists:
#         if user_data["stu_id'"]:
#              stu_exists["stu_id"]=user_data["stu_id"]
#         if user_data["stu_name"]:
#             stu_exists["stu_name"]=user_data["stu_name"]
#         if user_data["stu_branch"]:
#             stu_exists["stu_branch"]=user_data["stu_branch"]
#         if user_data["stu_mob"]:
#             stu_exists["stu_mob"]=user_data["stu_mob"]
#         stu_exists.save() 
        
#         return JsonResponse({"success":"user updated!!"})  
#     except:
#         return JsonResponse({"error":"user not found"})


# @csrf_exempt
# def update_user(req, id):
#     try:
#         user_data = json.loads(req.body)
#     except json.JSONDecodeError:
#         return JsonResponse({"error": "Invalid JSON"})

#     try:
#         student = Student.objects.get(stu_id=id)
#     except Student.DoesNotExist:
#         return JsonResponse({"error": "User not found"})

#     # Update only the fields provided in the request
#     if "stu_id" in user_data:
#         student.stu_id = user_data["stu_id"]
#     if "stu_name" in user_data:
#         student.stu_name = user_data["stu_name"]
#     if "stu_branch" in user_data:
#         student.stu_branch = user_data["stu_branch"]
#     if "stu_mob" in user_data:
#         student.stu_mob = user_data["stu_mob"]

#     student.save()  # Save changes to DB
#     return JsonResponse({"success": "User updated!!"})
        
    
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