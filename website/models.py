from django.db import models
from django.contrib.auth.models import User
from django.db import connections


# Create your models here.


class extendeduser(models.Model):
    address = models.CharField(max_length=30, blank=True)
    age = models.IntegerField()
    dob = models.CharField(max_length=30, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)



class Patients_detail(models.Model):
    Symptom1 = models.CharField(max_length=100, blank=True, null=True)
    Symptom2 = models.CharField(max_length=100, blank=True, null=True)
    Symptom3 = models.CharField(max_length=100, blank=True, null=True)
    Symptom4 = models.CharField(max_length=100, blank=True, null=True)
    Symptom5 = models.CharField(max_length=100, blank=True, null=True)
    suspected_Diseases = models.CharField(max_length=100, blank=True, null=True)
    suggested_doctor = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    


class doctor(models.Model):
    Doctor_name = models.CharField(max_length=100, blank=True, null=True)
    Department = models.CharField(max_length=100, blank=True, null=True)
    Detail = models.CharField(max_length=100, blank=True, null=True)
    number = models.CharField(max_length=100, blank=True, null=True)
   
    

   







