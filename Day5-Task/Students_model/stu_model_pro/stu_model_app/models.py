from django.db import models

# Create your models here.
class Stundent_details(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    age=models.IntegerField()
    roll_num=models.IntegerField()