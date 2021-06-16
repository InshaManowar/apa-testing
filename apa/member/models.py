from django.core.files.storage import default_storage
from django.db import models


def upload_location(instance, filename):
	file_path = 'member/{first_name}-{filename}'.format(
     first_name=str(instance.first_name), filename=filename)
	return file_path

GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
    (2, 'not specified'),
)

class Member(models.Model):
    first_name= models.CharField(max_length=50, default='', blank=False)
    last_name= models.CharField(max_length=50, default='', blank=False)
    dob=models.DateField(blank=False, default='yyyy-mm-dd')
    gender = models.IntegerField(choices=GENDER_CHOICES, default=None)

    email=models.EmailField(max_length=250, default=None, null=False, blank=False)
    mobile1=models.CharField(max_length=10, default='', null=False)
    mobile2=models.CharField(max_length=10, default='', null=True, blank=True)
    email=models.CharField(max_length=250, default=None, null=False, blank=False )
    
    address_1 = models.CharField(default='none', max_length=128)
    city = models.CharField(default=None, max_length=64)
    state = models.CharField(max_length=250, default=None, null=False, blank=False)
    zip_code = models.CharField(default=None, max_length=10)
    
    address_2 = models.CharField(default=None, max_length=128, blank=True)
    city2 = models.CharField(default=None, max_length=64)
    state2 = models.CharField(max_length=250, default=None, null=False, blank=False)
    zip_code2 = models.CharField(default=None, max_length=10)
    
    college=models.CharField(default=None, null=True, blank=True, max_length=500)
    degree=models.CharField(max_length=500, default=None)
    year_of_passing=models.CharField(max_length=4, default=None)
    
    university=models.CharField(default=None,max_length=500, null=True, blank=True)
    
    
    special_training=models.TextField(default=None, null=True, blank=True)
    council_reg_no=models.CharField(default='a-00000-b-1', max_length=12)
    council_reg_date=models.DateField( default='yyyy-mm-dd')
    council_name=models.CharField(max_length=500, default='')
    
    experience_years=models.CharField(default=None, max_length=4)
    private_practice=models.TextField(default=None, null=True)
    teacher=models.TextField(default=None)
    
    reference=models.TextField(default=None, null=True, blank=True)
    research_work=models.TextField(default=None, null=True, blank=True)
    
    
    profile_photo=models.FileField(default=None, upload_to=upload_location)
    registration_certificate=models.FileField(default=None, upload_to=upload_location)
    degree_certificate=models.FileField(default=None, upload_to=upload_location)
    postgraduate_certificate=models.FileField(default=None, upload_to=upload_location)
    remarks=models.TextField(default=None, null=True, blank=True)



