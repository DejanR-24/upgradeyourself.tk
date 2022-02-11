from django.contrib import admin
from .models import Client, Employee, Psychologist

class ClientAdmin(admin.ModelAdmin):
        list_display=('user','phonenumber', 'birthdate', 'gender')

class EmployeeAdmin(admin.ModelAdmin):
        list_display=('user','phonenumber', 'profile_picture')

class PsychologistAdmin(admin.ModelAdmin):
        list_display=('employee','bio')

admin.site.register(Client,ClientAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Psychologist,PsychologistAdmin)