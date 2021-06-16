from django.contrib import admin
from .models import Member
# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'mobile1', 'email','council_reg_no')  
    list_filter = ("council_reg_no","email","first_name") 
    search_fields = ['first_name', 'last_name', 'mobile1', 'email','council_reg_no']
    
admin.site.register(Member, MemberAdmin)