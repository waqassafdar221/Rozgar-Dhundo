from django.contrib import admin

from app.models import Author, JobPost, Location, Skills



class JobAdmin(admin.ModelAdmin):
    list_display = ('title','date','last_date','salary',)
    list_filter = ('date','salary','last_date')
    search_fields =['title']
    search_help_text ='Write query and hit enter'


# Register your models here.
admin.site.register(JobPost,)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skills)