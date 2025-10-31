from django.shortcuts import render
from .models import Student
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .serializers import StudentSerializer 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return JsonResponse({
                'message': 'Login successful!',
                'refresh_token': str(refresh),
                'access_token': str(refresh.access_token),
            })
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)
# @csrf_exempt
# def reg_user(req):
#     if req.method == "POST":
#         user_data = json.loads(req.body)
#         serialized_data = StudentSerializer(data=user_data, partial=True)
#         if serialized_data.is_valid():
#             serialized_data.save()
#             return JsonResponse({
#                 "message": "Student registered successfully",
#                 "data": serialized_data.data
#             })
#         else:
#             return JsonResponse(serialized_data.errors, status=400)

# @csrf_exempt
# def get_users(req):
#     if req.method == "GET":
#         all_data = Student.objects.all()
#         serialized_data = StudentSerializer(all_data, many=True)
#         return JsonResponse({"data": serialized_data.data}, safe=False)

# @csrf_exempt
# def delete_user(req, id):
#     if req.method == "DELETE":
#         try:
#             existing_stu = Student.objects.get(stu_id=id)
#             existing_stu.delete()
#             return JsonResponse({"success": "User deleted!"})
#         except Student.DoesNotExist:
#             return JsonResponse({"error": "User not found!"}, status=404)
