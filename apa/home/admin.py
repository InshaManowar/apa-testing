
from django.contrib import admin
from django.core.mail import (send_mail, BadHeaderError, EmailMessage)
from django.utils.safestring import mark_safe
import threading
from django.conf import settings
from django.http import HttpResponse
from .models import GalleryImage, Gallery, Video, VideoDisplay,  UpcomingEvents, ResourcesBooks, ResourcesLinks, ResourcesCategory

#gallery

class GalleryImageAdmin(admin.StackedInline):
    model = GalleryImage
 
class GalleryAdmin(admin.ModelAdmin):
    inlines = [GalleryImageAdmin]
    list_display=('title',)
    class Meta:
       model = Gallery
 
@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    pass

admin.site.register (Gallery, GalleryAdmin)

#Videos

class VideoDisplayAdmin(admin.StackedInline):
    model = VideoDisplay
    
 
class VideoAdmin(admin.ModelAdmin):
    inlines = [VideoDisplayAdmin]
    list_display=('title','created_time',)
 
@admin.register(VideoDisplay)
class VideoDisplayAdmin(admin.ModelAdmin):
    pass
admin.site.register (Video, VideoAdmin)

#pop up

class UpcomingEventsAdmin(admin.ModelAdmin):
    list_display = ('event_title')  
    
admin.site.register(UpcomingEvents)

#Resources

class ResourcesBooksAdmin(admin.ModelAdmin):
    list_display = ('book_title', 'author_name','publisher_details')

admin.site.register(ResourcesBooks)

class ResourcesLinksAdmin(admin.StackedInline):
    model = ResourcesLinks
 
class ResourcesCategoryAdmin(admin.ModelAdmin):
    inlines = [ResourcesLinksAdmin]
    class Meta:
       model = ResourcesCategory
 
@admin.register(ResourcesLinks)
class ResourcesLinksAdmin(admin.ModelAdmin):
    pass

admin.site.register (ResourcesCategory, ResourcesCategoryAdmin)

