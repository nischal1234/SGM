from django.contrib.auth.decorators import login_required
from app.models import Employee,Company,employee_company_relation

@login_required(login_url='login')
class search():
    def __init__(self,request,companyname,employename):
        self.companyname=companyname
        self.employename=employename

    def search_by_company(self,request,companyname):
        data=Company.objects.all()
        if companyname in data:
            return True
        else:
            return False
    def search_by_employe(self,request,employename):
        data=Employee.objects.all()
        if employename in data:
            return True
        else:
            return False
            