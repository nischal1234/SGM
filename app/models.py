from django.db import models
from phone_field import PhoneField

# Create your models here.
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


#save function    
    def datainp(last_ip):
        Employee.save()

    def __str__(self):
        return self.firstname + " " + self.lastname
    @staticmethod
    def get_member_by_email(username):
        try:
            return Employee.objects.get(username=username)
        except:
            return False

    def isExists(self):
        if Employee.objects.filter(username = self.username):
            return True

        return  False