
from django.contrib.messages.api import error
from app.models import Employee
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.hashers import  check_password
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

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
					return render(request,'app/login.html')
				
		
			
		
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
		return render(request,'app/dashboard.html')
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
		ins=Employee()
		Employee.objects.create(
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
			citizenship=citizenship)
		
		ins.save()

		return render(
            'app/guard_add.html',
            {'message': 'Update Success', })



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



login_required(login_url='login')
def view_guards(request):
	if request.user.is_authenticated:
		employeesdata=Employee.objects.all()

		return render(request,'app/view_guard.html',{'employee':employeesdata})
	else:
		return render(request, 'app/login.html')

