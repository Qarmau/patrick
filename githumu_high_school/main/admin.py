from django.contrib import admin
from .models import *

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title', 'description')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title', 'content')

@admin.register(CalendarEvent)
class CalendarEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title',)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    pass

@admin.register(Administrator)
class AdministratorAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'order')
    list_editable = ('order',)

@admin.register(TeachingStaff)
class TeachingStaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'role', 'subjects', 'order')
    list_editable = ('order',)

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('year', 'university_admission_rate')

@admin.register(CoCurricularAward)
class CoCurricularAwardAdmin(admin.ModelAdmin):
    list_display = ('title', 'year')

class HolidayAssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'grade', 'subject','title', 'description','year','author', 'date_uploaded')
    list_filter = ('grade', 'subject', 'year')
    search_fields = ('title', 'subject')

admin.site.register(HolidayAssignment, HolidayAssignmentAdmin)


@admin.register(BackgroundImage)
class BackgroundImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'order')
    list_editable = ('order',)