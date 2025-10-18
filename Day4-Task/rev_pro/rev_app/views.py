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
        user_data=json.loads(req.body) #coverting Json->string (details)
        for user in details:
            if user_data["id"] == user["id"]:
                return JsonResponse({"msg":"already exists"})
        details.append(user_data)
        print(details)
        return JsonResponse({"msg":"user successfully added"})
    else:
        return JsonResponse({"msg": "only POST method allowed"})


# patch method
@csrf_exempt
def patch_method(req):
    if req.method == "PATCH":
        user_data=json.loads(req.body)  # decode request body
        user_id = user_data.get("id")  # get id to identify which user to update
        for user in details:
            if user["id"] == user_id:  # find the matching user
                for key, value in user_data.items():
                    if key != "id":
                        user[key] = value
                print(details)
                return JsonResponse({"msg": "user updated successfully", "updated_data": user})
        
        return JsonResponse({"msg": "user not found"})
    else:
        return JsonResponse({"msg": "only PATCH method allowed"})

#put method
@csrf_exempt
def put_method(req):
    if req.method == "PUT":
        user_data = json.loads(req.body)  # decode request body
        user_id = user_data.get("id")  # get id to identify which user to update
        for user in details:
            if user["id"] == user_id:  # find matching user
                # Replace the entire record with new data
                user.clear()        # remove old data
                user.update(user_data)  # replace with new data
                print(details)
                return JsonResponse({"msg": "user replaced successfully", "updated_data": user})

        return JsonResponse({"msg": "user not found"})
    else:
        return JsonResponse({"msg": "only PUT method allowed"})

#delete method
def delete_method(req):
    if req.method == "DELETE":
        user_data = json.loads(req.body)
        user_id = user_data.get("id")
        for user in details:
            if user["id"] == user_id:  # find matching user
                details.remove(user)
                print(details)
                return JsonResponse({"msg": "user deleted successfully", "deleted_user": user})
            return JsonResponse({"msg": "user not found"}, status=404)

    else:
        return JsonResponse({"msg": "only DELETE method allowed"}, status=405)