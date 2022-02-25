from django.contrib import admin

from .models import Schedule,Therapy, Fullcalendar

class ScheduleAdmin(admin.ModelAdmin):
        list_display=('id','time')

class FullcalendarAdmin(admin.ModelAdmin):
        list_display=('title','start','end','psychologist_id')

class TherapyAdmin(admin.ModelAdmin):
        list_display=('date','schedule_id','psychologist_id','client_id')

admin.site.register(Schedule,ScheduleAdmin)
admin.site.register(Fullcalendar,FullcalendarAdmin)
admin.site.register(Therapy,TherapyAdmin)