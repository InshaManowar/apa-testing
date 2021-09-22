from django.conf.urls import url
from django.urls import path, include
from home import views
from django.conf.urls import handler404, handler500
import home


app_name = 'home'

urlpatterns = [
    path('', views.upcomingEvents_view, name='home'),
    path('ayurved-proctology-association/', views.aboutus, name='aboutus'),
    path('visions/', views.visions, name='visions'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('videos/', views.video_view, name='video'),
    path('contactus/', views.contactus, name='contactus'),
    path('resources/', views.resource_view, name='resource'),

]
    
handler404 = home.views.error_404
handler500 = home.views.error_500