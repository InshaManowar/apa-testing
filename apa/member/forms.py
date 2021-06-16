from django import forms
from django.db import models
from django.db.models import fields
from .models import Member

class MembershipForm(forms.ModelForm):
    email = forms.EmailField(max_length=300, help_text='Add a valid email address')
    
    class Meta:
        model = Member
        fields='__all__'    
        labels = {
            'dob':('Date of birth'),
            'mobile1':('Your mobile number 1'),
            'year_of_passing':('Year of passing college'),
            'mobile2':('Your mobile number 2'),
            'college':('Name of your college'),
            'university':('Name of your university'),
            'special_training':('Any special training'),
            'council_reg_no':('Council registration number'),
            'council_reg_date':('Council registration date'),
            'special_training':('Any special training'),
            'mobile2':('Your mobile number 2'),
            'degree':('Your college degree name, e.g BAMS, MS, MD'),
            'experience_name':('Years of experience'),
            'private_practice':('About your private practice'),
            'teacher':('About your teaching experience'),
            'reference':('Any references'),
            'Research_work':('About your research work'),
            'address_1':('Resident Address'),
            'address_2':('Clinic Address'),
            'city2':('City your clinic is located in'),
            'state2':('State your clinic is located in'),
            'zip_code2':('Zip code')
        }
        
    