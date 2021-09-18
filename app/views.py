
from django.contrib.messages.api import error
from .forms import *
from . import models
from app.models import Employee,Company,employee_company_relation
from django.shortcuts import render, redirect 
from django.http import HttpResponse, request
from django.forms import inlineformset_factory
from django.contrib.auth.hashers import  check_password
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from app.search import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.translation import gettext as _
from django.core.files.storage import FileSystemStorage

# Create your views here.
@csrf_exempt
def home(request):
	if request.user.is_authenticated:
		
		return redirect('dashboard/')
	else:
		if request.method == 'POST':

			username = request.POST.get('username')
			password =request.POST.get('password')
			user=authenticate(username=username,password=password)
			print('here i am')
			print(user)
			if user is not None:
					login(request,user)
					
					return render(request,'app/dashboard.html')
   				 # A backend authenticated the credentials
			else:
				message='Username or Password is wrong!!'
				return render(request,'app/login.html',{'message':message})
				
		
			
		
				#error_message='username or password is incorrect!!'
				
		#messages.info(request, 'last executed')
		error_message='username or password is incorrect!!'
		return render(request, 'app/login.html', {error:error_message})
		
@login_required(login_url='login')
def logoutUser(request):
	logout(request)
	return redirect('login')
login_required(login_url='login')
def dashboard(request):
	if request.user.is_authenticated:
		count = Employee.objects.count()
		return render(request,'app/dashboard.html',{
        'count' : count
    })
	else:
		return render(request, 'app/login.html')


@csrf_exempt
@login_required(login_url='login')
def guard_add(request):
	
	if request.method=='POST':
		fname=request.POST.get('fname')
		mname=request.POST.get('sname')
		lname=request.POST.get('lname')
		paddress=request.POST.get('paddress')
		taddress=request.POST.get('taddress')
		dob=request.POST.get('dob')
		joindate=request.POST.get('joindate')
		exyear=request.POST.get('exyear')
		pnumber=request.POST.get('pnumber')
		snumber=request.POST.get('snumber')
		citizenship=request.POST.get('citinum')
		fathername=request.POST.get('fathername')
		grandfather=request.POST.get('gname')
		education=request.POST.get('eduquali')
		assign=request.POST.get('apost')
		pastcompany=request.POST.get('pastcname')
		pan=request.POST.get('pannumber')
		height=request.POST.get('hguard')
		skin=request.POST.get('skincolor')
		gender=request.POST.get('gender')
		maritual=request.POST.get('mstatus')
		blood=request.POST.get('bgroup')
		if Employee.objects.filter(firstname=fname,middlename=mname,lastname=lname,fathername=fathername).exists() or Employee.objects.filter(citizenship=citizenship).exists():
			messages="Security guard is already registered !!"
			return render(request,'app/guard_add.html',{'message_does': messages})
		
		
		else:
			ins=Employee()
			p=Employee(
				firstname=fname,
				middlename=mname,
				lastname=lname,
				permanent_address=paddress,
				temporary_address=taddress,
				dateofbirth=dob,
				joindate=joindate,
				expyear=exyear,
				pnumber=pnumber,
				snumber=snumber,
				citizenship=citizenship,
				fathername=fathername,
				grandfathername=grandfather,
				education=education,
				assignpost=assign,
				pastcname=pastcompany,
				pannumber=pan,
				height=height,
				skincolor=skin,
				gender=gender,
				maritual=maritual,
				bloodgroup=blood	
				)

			p.save()
			
			
			messages="Guard details has been saved successfully !!"
			
			return render(request,
				'app/guard_add.html',
				{'message_doesnt': messages })



	else:
		return render(request,'app/guard_add.html')
	
	return render(request,'app/guard_add.html')

def get_ip_address(request):
    """ use requestobject to fetch client machine's IP Address """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')    ### Real IP address of client Machine
    return ip   



@login_required(login_url='login')
def view_guards(request):
	if request.user.is_authenticated:
		employeesdata=Employee.objects.all()

		return render(request,'app/view_guard.html',{'employee':employeesdata})
	else:
		return render(request, 'app/login.html')
@login_required(login_url='login')
def profile(request,id):
	profileid=id
	companylist=Company.objects.all()
	data=Employee.objects.get(pk=id)
	#print(data)
	
#	return render(request,'app/profile.html',{'profileid':profileid})
	return render(request,'app/profile.html',context={'data':data,'company':companylist})

@login_required(login_url='login')
def addcompany(request):
	if request.method=='POST':
		companyname=request.POST.get('cpname')
		address=request.POST.get('cpaddress')
		branchname=request.POST.get('branchname')
		cppannumber=request.POST.get('cppannumber')
		cpwebsite=request.POST.get('cpwebsite')
		cpphnnumber=request.POST.get('cpphnnumber')
		
		if Company.objects.filter(companyname=companyname).exists() or Company.objects.filter(cpannumber=cppannumber).exists() :
			print("exist")
			message="already exist this company! Please check your input data"
			return render(request,'app/add_company.html',{'messages_does':message})
		

		else:
			ins=Company()
			Company.objects.create(companyname=companyname,
			location=branchname,
			district=address,
			website=cpwebsite,
			telephone=cpphnnumber,
			cpannumber=cppannumber	
			
			)	
			print("not exists")
			message="Company registered successfully! "
			return render(request,'app/add_company.html',{'messages_doesnt':message})
			


	else:
		print("executed")
		return render(request,'app/add_company.html')

@login_required(login_url='login')
def viewcompany(request):
	if request.user.is_authenticated:
		companydata=Company.objects.all()

		return render(request,'app/view_company.html',{'company':companydata})
	else:
		return render(request, 'app/login.html')


@login_required(login_url='login')
def feedback(request):
	return render(request,'app/feedback.html')

@login_required(login_url='login')
def search(request):
	ids=request.POST.get('searchopt')
	print(ids)
	data=request.POST.get('searchdata')
	if ids=='Guard':
		
		datas=Employee.objects.filter(firstname=data)
		print(datas)
		return render(request,'app/search.html',{'datas':datas})
	elif ids=='Company':
		datas=Company.objects.filter(companyname=data)
		return render(request,'app/search.html',{'datas':datas})

	#now use same as above elif statement as ids=='Age Below 50' ,,,,it will works 
	elif ids=='Age Below 50':
		datas=Employee.objects.filter(dateofbirth=data)
	message="please select one and enter the keyword"
	return render(request,'app/search.html',{'message':message})


@login_required(login_url='login')
def companyprofile(request,id):
	if request.method=='POST':

		findcompany=Company.objects.get(pk=id)
		uploadedreg = request.FILES['cpreg']
		uploadedpan = request.FILES['cppanimage']
		uploadedagree = request.FILES['cpagreement']
		uploadedother = request.FILES['cpother']

		#code for saving in database
		findcompany.regfiles=uploadedreg
		findcompany.save()
		findcompany.panvat=uploadedpan
		findcompany.save()			
		findcompany.other=uploadedagree
		findcompany.save()
		findcompany.agree=uploadedother
		findcompany.save()
	
		
		
	
		
		
	
	#employee_list_by_company=employee_company_relation()
	idvalue=employee_company_relation.objects.filter(company_details=id).values('employee_details')
	#newvalue=employee_company_relation.objects.filter(pk=)
	print(idvalue)
	employee_data=[]
	for ele in idvalue:
		for key, value in ele.items():
		#	print(value)
			employee_data.append(Employee.objects.get(pk=value))
			#print(employee)
	print(employee_data)
	#now find out all employee id using for loop in idvalue dict. then extract all data associated in that id.

	
	#employee=employee_company_relation.objects.get(pk=idvalue)
	
	data=Company.objects.get(pk=id)
	print(data)
	#print(data)
#	return render(request,'app/profile.html',{'profileid':profileid})
	return render(request,'app/companyprofile.html',{'data':data,'employee_list':employee_data})


@login_required(login_url='login')
def company_update(request,id):
	companyname=request.POST.get('cpname')
	address=request.POST.get('cpaddress')
	branchname=request.POST.get('branchname')
	cppannumber=request.POST.get('cppannumber')
	cpwebsite=request.POST.get('cpwebsite')
	cpphnnumber=request.POST.get('cpphnnumber')
	if Company.objects.filter(companyname=companyname).exclude(pk=id).exists() or Company.objects.filter(cpannumber=cppannumber).exclude(pk=id).exists() :
			print("exist")
			message="already exist this company! Please check your input data"
			data=Company.objects.get(pk=id)
			return render(request,'app/companyprofile.html',{'messages_doesnt':message, 'data':data})
			
		

	else:
			ins=Company.objects.get(pk=id)
			ins.companyname=companyname
			ins.save()
			ins.location=branchname
			ins.save()
			ins.district=address
			ins.save()
			ins.website=cpwebsite
			ins.save()
			ins.telephone=cpphnnumber
			ins.save()
			ins.cpannumber=cppannumber	
			ins.save()
			
			print("not exists")
			message="Company Modified successfully! "
			data=Company.objects.get(pk=id)
			return render(request,'app/companyprofile.html',{'messages_doesnt':message, 'data':data})
	print(companyname)
	print(id)
	companydata=Company.objects.all()

	return render(request,'app/view_company.html',{'company':companydata})

@login_required(login_url='login')
def choosecompany(request,id):
	if request.method=='POST':
		#print(id)
		#.....................company id extraction.......................
		cname=request.POST.get('companynamedata')
		print(cname)
		idcompany = Company.objects.get(companyname=cname).id
		print(idcompany)
		companydetails=Company.objects.get(companyname=cname)
		#.................................................................
		#print(companydetails)

		#................Employee id extraction...........................
		employeedetails=Employee.objects.get(pk=id)
		relation=employee_company_relation()
		employee_posting_history.objects.create(employee_id=employeedetails,company_details=companydetails)
		#...................................................................
		if employee_company_relation.objects.filter(employee_details=employeedetails).exists():
			idnumber=employee_company_relation.objects.get(employee_details=employeedetails)
			idnumber.company_details=companydetails
			idnumber.save()
			companylist=Company.objects.all()
			data=Employee.objects.get(pk=id)
			return render(request,'app/profile.html',context={'data':data,'company':companylist})
		else:
			relation=employee_company_relation()
			employee_company_relation.objects.create(employee_details=employeedetails,company_details=companydetails)
			
			companylist=Company.objects.all()
			data=Employee.objects.get(pk=id)
			return render(request,'app/profile.html',context={'data':data,'company':companylist})

				
	companylist=Company.objects.all()
	data=Employee.objects.get(pk=id)
		#print(data)
		
#	return render(request,'app/profile.html',{'profileid':profileid})
	return render(request,'app/profile.html',context={'data':data,'company':companylist})

@login_required(login_url='login')
def guard_update(request,id):
	if request.method=='POST':
		fname=request.POST.get('fname')
		mname=request.POST.get('sname')
		lname=request.POST.get('lname')
		paddress=request.POST.get('paddress')
		taddress=request.POST.get('taddress')
		dob=request.POST.get('dob')
		joindate=request.POST.get('joindate')
		exyear=request.POST.get('exyear')
		pnumber=request.POST.get('pnumber')
		snumber=request.POST.get('snumber')
		citizenship=request.POST.get('citinum')
		fathername=request.POST.get('fathername')
		grandfather=request.POST.get('gname')
		education=request.POST.get('eduquali')
		assign=request.POST.get('apost')
		pastcompany=request.POST.get('pastcname')
		pan=request.POST.get('pannumber')
		height=request.POST.get('hguard')
		skin=request.POST.get('skincolor')
		gender=request.POST.get('gender')
		maritual=request.POST.get('mstatus')
		blood=request.POST.get('bgroup')
		if Employee.objects.filter(firstname=fname,middlename=mname,lastname=lname,fathername=fathername).exclude(pk=id).exists() and Employee.objects.filter(citizenship=citizenship).exclude(pk=id).exists():
			messages="Security guard is already registered !!"
			data=Employee.objects.get(pk=id)
			return render(request,'app/guard_add.html',{'message_does': messages, 'data':data})
		
		
		else:
			ins=Employee.objects.get(pk=id)
			
			ins.firstname=fname
			ins.save()
			ins.middlename=mname
			ins.save()
			ins.lastname=lname
			ins.save()
			ins.permanent_address=paddress
			ins.save()
			ins.temporary_address=taddress
			ins.save()
			ins.dateofbirth=dob
			ins.save()
			ins.joindate=joindate
			ins.save()
			ins.expyear=exyear
			ins.save()
			ins.pnumber=pnumber
			ins.save()
			ins.snumber=snumber
			ins.save()
			ins.citizenship=citizenship
			ins.save()
			ins.fathername=fathername
			ins.save()
			ins.grandfathername=grandfather
			ins.save()
			ins.education=education
			ins.save()
			ins.assignpost=assign
			ins.save()
			ins.pastcname=pastcompany
			ins.save()
			ins.pannumber=pan
			ins.save()
			ins.height=height
			ins.save()
			ins.skincolor=skin
			ins.save()
			ins.gender=gender
			ins.save()
			ins.maritual=maritual
			ins.save()
			ins.bloodgroup=blood
			ins.save()
					
			
			messages="Guard details has been updated successfully !!"
			data=Employee.objects.get(pk=id)
			return render(request,
				'app/guard_add.html',
				{'message_doesnt': messages , 'data':data})



	else:
		return render(request,'app/guard_add.html')

	return render(request,'app/profile.html',{'company':companydata})