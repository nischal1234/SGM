from datetime import datetime
from django.db import models
from phone_field import PhoneField
import datetime
import time
# Create your models here.
class Company(models.Model):
    companyname=models.CharField(max_length=50)
    location=models.CharField(max_length=40)
    district=models.CharField(max_length=10)
    website=models.URLField(max_length=20)
    telephone=models.CharField(max_length=15)
    cpannumber=models.CharField(max_length=15)
    regfiles=models.FileField(upload_to='company_documents/' ,null=True)
    panvat=models.FileField(upload_to='company_documents/',null=True)
    other=models.FileField(upload_to='company_documents/',null=True)
    agree=models.FileField(upload_to='company_documents/',null=True)

    def __str__(self):
        return self.companyname




class Employee(models.Model):
    firstname=models.CharField(max_length=30)
    middlename=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    permanent_address=models.CharField(max_length=12)
    temporary_address=models.CharField(max_length=12)
    dateofbirth=models.DateTimeField(null=True)
    joindate=models.DateTimeField(null=True)
    expyear=models.IntegerField(null=True)
    pnumber=models.CharField(max_length=13)
    snumber=models.CharField(max_length=13)
    citizenship=models.CharField(max_length=15)
    fathername=models.CharField(max_length=30)
    grandfathername=models.CharField(max_length=30)
    education=models.CharField(max_length=30)
    assignpost=models.CharField(max_length=30)
    pastcname=models.CharField(max_length=40)
    pannumber=models.CharField(max_length=20)
    height=models.CharField(max_length=5)
    skincolor=models.CharField(max_length=10)
    gender=models.CharField(max_length=10)
    maritual=models.CharField(max_length=10)
    bloodgroup=models.CharField(max_length=5)
    gphoto=models.FileField(upload_to='guard_documents/',null=True)
    gagree=models.FileField(upload_to='guard_documents/',null=True)
    gothers=models.FileField(upload_to='guard_documents/',null=True)
    gpan=models.FileField(upload_to='guard_documents/',null=True)

#save function    
   

    def __str__(self):
        return self.firstname + " " + self.lastname

    @property
    def age(self):
        today=datetime.datetime.today()
        age= today.year-self.dateofbirth.year-((today.month,today.day)<(self.dateofbirth.month,self.dateofbirth.day))
        return age
#company details
# 
class employee_company_relation(models.Model):
      employee_details=models.ForeignKey('Employee', null=True, on_delete=models.CASCADE)
      company_details=models.ForeignKey('Company', null=True, on_delete=models.CASCADE)

class employee_posting_history(models.Model):
    employee_id=models.ForeignKey('Employee', null=True, on_delete=models.CASCADE)
    company_details=models.ForeignKey('Company', null=True, on_delete=models.CASCADE)
    post_date=models.DateField(auto_now_add=True)
    

    

