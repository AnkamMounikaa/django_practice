from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def user_methods(request):
    if request.method == 'GET':
        return JsonResponse({"message": "GET method - fetching data"})

    elif request.method == 'POST':
        return JsonResponse({"message": "POST method - creating data"})

    elif request.method == 'PUT':
        return JsonResponse({"message": "PUT method - updating all fields"})

    elif request.method == 'PATCH':
        return JsonResponse({"message": "PATCH method - updating some fields"})

    elif request.method == 'DELETE':
        return JsonResponse({"message": "DELETE method - deleting data"})
