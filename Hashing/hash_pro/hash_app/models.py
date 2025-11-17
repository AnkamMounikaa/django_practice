from django.db import models

# Create your models here.
class emp_data(models.Model):
    emp_name=models.CharField(max_length=20)
    emp_salary=models.CharField(max_length=20)
    emp_role=models.CharField(max_length=100)