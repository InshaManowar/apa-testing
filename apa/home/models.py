
from django.db import models
from django.dispatch import receiver
from datetime import datetime


def upload_location(instance, filename, *kwargs):
	file_path = 'home/{gallery}-{filename}'.format(
     gallery=str(instance.gallery), filename=filename)
	return file_path

class Gallery(models.Model):
    title = models.CharField(max_length=250)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural=verbose_name='All gallery'
    
class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, default=None, on_delete=models.CASCADE)
    photo = models.ImageField (upload_to = upload_location, default = None, blank=True)
    class Meta:
        verbose_name_plural='Gallery Images'
    def __str__(self):
        return self.gallery.title
    
class Video(models.Model):
    title = models.CharField(max_length=250)
    created_time = models.DateTimeField( default= datetime.now())
    class Meta:
            ordering = ['-created_time', ]
    def __str__(self):
        return self.title
   
    
class VideoDisplay(models.Model):
    videos = models.ForeignKey(Video, default=None, on_delete=models.CASCADE)
    display = models.TextField( default = None, blank=True)
 

    
class VideoSidebar(models.Model):
    videos = models.ForeignKey(Video, default=None, on_delete=models.CASCADE)
    display_sidebar = models.TextField( default = None, blank=True)
    
    
class UpcomingEvents(models.Model):
    event_name = models.CharField(default=None, blank=False, max_length=150)
    event_info= models.TextField(default=None, blank=False)
    class Meta:
        verbose_name_plural=verbose_name='Upcoming Events pop up'
    def __str__(self):
        return self.event_name
    
class ResourcesCategory(models.Model):
    resource_title = models.CharField(default=None, blank=False, max_length=250)
    class Meta:
        verbose_name_plural='Resource Categories'
    def __str__(self):
        return self.resource_title
    
class ResourcesLinks(models.Model):
    links = models.ForeignKey(ResourcesCategory, default=None, on_delete=models.CASCADE)
    link_of_resource = models.TextField(default=None, blank=False)
    clickable_text = models.TextField(default='Click here', blank=False)
    class Meta:
        verbose_name_plural=verbose_name='Resource Links'
    def __str__(self):
        return self.clickable_text

        
class ResourcesBooks(models.Model):
    book_title = models.CharField(default=None, blank=False, max_length=250)
    pdf_link = models.TextField(default=None, blank=False)
    author_name = models.TextField(default=None, blank=False)
    publisher_detail = models.TextField(default=None, blank=True)
    details = models.TextField(default=None, blank=True)
    clickable_text = models.TextField(default='Download pdf', blank=False)
    class Meta:
        verbose_name_plural=verbose_name='Resource Books'
    def __str__(self):
        return self.book_title
    