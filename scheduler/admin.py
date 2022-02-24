from django.contrib import admin

from .models import Schedule,Therapy

class ScheduleAdmin(admin.ModelAdmin):
        list_display=('id','time')

class TherapyAdmin(admin.ModelAdmin):
        list_display=('date','shedule_id','psychologist_id','client_id')

admin.site.register(Schedule,ScheduleAdmin)
admin.site.register(Therapy,TherapyAdmin)