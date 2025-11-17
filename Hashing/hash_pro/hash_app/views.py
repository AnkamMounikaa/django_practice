from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from hash_app.models import emp_data
import bcrypt

# Create your views here.
def get_user(req):
    data=emp_data.objects.all() #to fetch all the records from the db and 
    #the data is in querset binary form so using orm values method we convert it as a dictionaries
    # print(data)
    details=data.values()
    # print(details)
    #print(details) it converts as dictionary but we have to display in browser 
    # #we need convert as python lists
   
    return JsonResponse({"Emp_details":list(details)})
@csrf_exempt
def reg_user(req):
    data=json.loads(req.body)
    emp_name=data.get('name')
    emp_salary=data.get('salary')
    emp_role=data.get('role')
    role=emp_role.encode('utf-8')
    salt=bcrypt.gensalt(rounds=12)
    encrypt_role=bcrypt.hashpw(password=role,salt=salt)
    
    emp_id=data.get('id')
    existing_emp = emp_data.objects.filter(id=emp_id)
    if existing_emp.exists():
        return HttpResponse("Employee already exists")
        
    else:
        table=emp_data.objects.create( emp_name = emp_name,emp_salary = emp_salary,
        emp_role = encrypt_role)
        return HttpResponse("emp registered successfully")

@csrf_exempt
def update_user(req,id):
    if req.method=='POST':
        data=json.loads(req.body)
        emp_id=data.get('id')
        emp=emp_data.objects.filter(id=id)
        # print(Emp_data.objects.all().values())
        # print(Emp_data.objects.filter(id=2).exists())
        if emp.exists():
              emp = emp.first()
              if data.get('name'):
                emp.name = data['name']
              if data.get('salary'):
                emp.salary = data['salary']
              if data.get('role'):
                emp.role = data['role']

              emp.save()
              return HttpResponse("Employee updated successfully")
        else:
            return HttpResponse("Employee not found")