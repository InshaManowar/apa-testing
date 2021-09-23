from django.db import models
from django.db.models.fields.related import ForeignKey
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver


def upload_location(instance, filename, *kwargs):
	file_path = 'events/{event}-{filename}'.format(
     event=str(instance.event), filename=filename)
	return file_path

STATUS = (
    (0,"Draft" ),
    (1,"Publish")
)

class Event(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    location = models.CharField(max_length=100)
    content = models.TextField(default='')
    subtitle = models.TextField(default='')
    startdate = models.DateTimeField()
    enddate = models.DateTimeField(default='')
    status = models.IntegerField(choices = STATUS, default=0)
    link = models.TextField(default=None)
    class Meta:
        ordering = ['startdate']

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-startdate',]
    
class EventImage(models.Model):
    event = models.ForeignKey(Event, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = upload_location, blank=True, default=None)
    

    def __str__(self):
        return self.event.title+' image'
 
class EventTable(models.Model):
    event = models.ForeignKey(Event, default=None, on_delete=models.CASCADE)
    start_date_for_day = models.DateTimeField()
    end_date_for_day = models.DateTimeField()
    title_for_day = models.CharField(default='', max_length=100)
    description_for_day = models.TextField(default='')
    
    def __str__(self):
        return self.event.title+' table'
    
class EventNew(models.Model):
    event = models.ForeignKey(Event, default=None, on_delete=models.CASCADE)
    title_of_event = models.CharField(default='', blank=False, max_length=120)
    short_description = models.TextField(default='', max_length=150)

    def __str__(self):
        return self.title_of_event
    class Meta:
        verbose_name='New Event'
        
    
class Speakers(models.Model):
    event = models.ForeignKey(Event, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='')
    photo = models.FileField(upload_to = upload_location, blank=True, default=None)
    details = models.TextField(default='', blank=True, null=True)
    
    
def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slugify(instance.title)
pre_save.connect(pre_save_blog_post_receiver, sender=Event)
