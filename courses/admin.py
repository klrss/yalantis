from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display=("id","name","begin","end","number")

# Register your models here.
admin.site.register(Course, CourseAdmin)