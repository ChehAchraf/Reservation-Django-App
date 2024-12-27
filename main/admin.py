from django.contrib import admin
from .models import Activities , ActivityCategory , Highlight , ActivityImage
admin.site.register(Activities)
admin.site.register(ActivityCategory)

class ActivityImageInline(admin.TabularInline):
    model = ActivityImage
    extra = 1

class HighlightInline(admin.TabularInline):  
    model = Activities.highlights.through  
    extra = 1  

class ActivitiesAdmin(admin.ModelAdmin):
    inlines = [HighlightInline]  
    list_display = ['title', 'description']  


admin.site.register(Highlight)
admin.site.register(ActivityImage)