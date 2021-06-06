from django.conf.urls import url
from django.urls import path, include
from home import views


app_name = 'home'

urlpatterns = [
    path('', views.upcomingEvents_view, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('visions/', views.visions, name='visions'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('videos/', views.video_view, name='video'),
    path('contactus/', views.contactus, name='contactus'),
    path('resources/', views.resource_view, name='resource'),

]
