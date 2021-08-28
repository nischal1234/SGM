from django import forms
from .models import *

class companyform(forms.ModelForm):
     class Meta:
        model = Company
        fields = ['regfiles' ,'panvat', 'other' , 'agree']
       