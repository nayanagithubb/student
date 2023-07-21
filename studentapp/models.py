from django.db import models

# Create your models here.
class Student(models.Model):
    StudentName=models.CharField(max_length=255)
    Address=models.TextField()
    Age=models.IntegerField()
    EmailID=models.EmailField()
    JoiningDate=models.DateField(auto_now_add=False,auto_now=False,blank=True)
    Qualification=models.CharField(max_length=255)
    Gender=models.CharField(max_length=255)
    MobileNumber=models.CharField(max_length=255) 
   
 