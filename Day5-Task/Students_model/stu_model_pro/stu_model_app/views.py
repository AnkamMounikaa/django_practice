from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Stundent_details

#GET
def get_details(request):
    if request.method=="GET":
        user=Stundent_details.objects.all()
        data=list(user.values())
        return JsonResponse({"data":list(data)})

#POST
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

#PUT 
@csrf_exempt
def updateuser(req,id):

    if req.method=='PUT':
        try:
            coder=Stundent_details.objects.get(id=id)

            user_data=Stundent_details.loads(req.body)

            idn=user_data["id"]
            namen=user_data["name"]
            agen=user_data["age"]

            coder.id=idn
            coder.name=namen
            coder.age=agen
            coder.save()
            return HttpResponse("user updated succesfully")
        
        except:
            return HttpResponse("user not found")


#DELETE
@csrf_exempt
def deleteuser(req,id):
    if req.method=='DELETE':
        try:
            coder=Stundent_details.objects.get(id=id)

            coder.delete()
            
            return HttpResponse("user deleted succesfully")
        except:
            return HttpResponse("user not found")