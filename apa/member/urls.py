from . import views
from django.urls import path

app_name = 'member'
urlpatterns = [
    path('', views.membership_form, name= 'membership'),
    path('confirm/', views.membershipConfirm_view, name= 'member_confirm'),

] 
