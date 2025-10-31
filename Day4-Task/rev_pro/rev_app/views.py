from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

details=[
    {"id":1, "name":"mounika","batch":42},
    {"id":2, "name":"satya","batch":41}
]
# Post Method
@csrf_exempt
def post_method(req):
    if req.method == "POST":
        user_data=json.loads(req.body) 
        for user in details:
            if user_data["id"] == user["id"]:
                return JsonResponse({"msg":"already exists"})
        details.append(user_data)
        print(details)
        return JsonResponse({"msg":"user successfully added"})
    else:
        return JsonResponse({"msg": "only POST method allowed"})

