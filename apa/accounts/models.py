from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from shortuuidfield import ShortUUIDField

def upload_location(instance, filename, *kwargs):
	file_path = 'accounts/{username}-{filename}'.format(
     username=str(instance.username), filename=filename)
	return file_path


class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_active = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class Account(AbstractBaseUser):
    uuid = ShortUUIDField(unique=True)
    email= models.EmailField(verbose_name="email", max_length=60, unique= True)
    username= models.CharField(max_length=30, unique= True)
    date_joined=models.DateTimeField(verbose_name='date joined',auto_now_add= True)
    last_login= models.DateTimeField(verbose_name='last login',auto_now= True)
    first_name= models.CharField(max_length=50, default='')
    last_name= models.CharField(max_length=50, default='')
    designation = models.CharField(max_length=150, default='')
    qualification = models.CharField(max_length=150, default='')
    address= models.TextField(max_length=150, default='')
    phone= PhoneNumberField(blank=True, help_text='Contact phone number')
    is_admin= models.BooleanField(default=True)
    is_active= models.BooleanField(default=False)
    is_staff= models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)
    profile_image=models.ImageField(upload_to=upload_location, blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = MyAccountManager()
    
    def __str__(self):
        return self.email

	# For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

