from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.ModelSerializer):
    class Meta:  ##provides info about the tables and fields
        model=Student
        # fields=["stu_id","stu_name"]
        fields="__all__"
        