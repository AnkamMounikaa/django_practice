from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import UserReg

# Create your views here.
def validate_file(file_obj):
    max_size = 5 * 1024 * 1024
    if file_obj.size > max_size:
        return False, 'File too large. Max size is 5MB.'
    allowed_types = ['image/jpeg', 'image/png']
    if file_obj.content_type not in allowed_types:
        return False, 'Invalid file type. Allowed: JPG, PNG'
    return True, 'Valid file'
@csrf_exempt
def reg_user(req):
    user_name=req.POST.get("name")
    user_email=req.POST.get("email")
    user_mob=req.POST.get("mob")
    file_obj=req.FILES["profile_pic"]
    is_valid_file,msg=validate_file(file_obj)
    if is_valid_file:
        pass 
    else:
        return HttpResponse (msg)    
    new_user=UserReg.objects.create(name=user_name,email=user_email,mobile=user_mob,pic=file_obj)
    return HttpResponse("reg!")
