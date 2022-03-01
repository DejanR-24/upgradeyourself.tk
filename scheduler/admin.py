from django.contrib import admin

from .models import GoesTo,ConfirmationStatus, WorkingHours,Therapy #Fullcalendar

class WorkingHoursAdmin(admin.ModelAdmin):
        list_display=('id','time')

class ConfirmationStatusAdmin(admin.ModelAdmin):
        list_display=('id','status')

# class FullcalendarAdmin(admin.ModelAdmin):
#         list_display=('title','start','end','psychologist_id')

class TherapyAdmin(admin.ModelAdmin):
        list_display=('date','workinghours','psychologist','client_id')

class GoesToAdmin(admin.ModelAdmin):
        list_display=('client_id','psychologist')

admin.site.register(WorkingHours,WorkingHoursAdmin)
admin.site.register(ConfirmationStatus,ConfirmationStatusAdmin)
#admin.site.register(Fullcalendar,FullcalendarAdmin)
admin.site.register(Therapy,TherapyAdmin)
admin.site.register(GoesTo,GoesToAdmin)