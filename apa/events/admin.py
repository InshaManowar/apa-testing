from django.contrib import admin
from .models import Event, EventImage, EventTable, EventNew, Speakers
# Register your models here.
class EventImageAdmin(admin.StackedInline):
    model = EventImage
    list_display = ('event')  
    
class SpeakersAdmin(admin.StackedInline):
    model = Speakers
    list_display = ('name')

class EventTableAdmin(admin.StackedInline):
    model = EventTable

class EventNewAdmin(admin.StackedInline):
    model = EventNew
    
    list_display = ('event','title_of_event')  

 
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'startdate','enddate')  
    list_filter = ("status",) 
    search_fields = ['title','content','startdate']  
    prepopulated_fields = {'slug': ('title',)}  
    inlines = [EventImageAdmin,EventTableAdmin, EventNewAdmin, SpeakersAdmin]
    
@admin.register(EventImage)
class EventImageAdmin(admin.ModelAdmin):
    pass
@admin.register(EventTable)
class EventTableAdmin(admin.ModelAdmin):
    list_display = ('event','title_for_day','start_date_for_day','end_date_for_day',)  

    pass
@admin.register(EventNew)
class EventNewAdmin(admin.ModelAdmin):
    pass
@admin.register(Speakers)
class SpeakersAdmin(admin.ModelAdmin):
    pass



admin.site.register(Event, EventAdmin) 
