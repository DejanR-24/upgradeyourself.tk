from django.contrib import admin
from .models import Client, Employee, Psychologist
from rest_framework_simplejwt import token_blacklist


class ClientAdmin(admin.ModelAdmin):
        list_display=('user','phonenumber', 'birthdate', 'gender')

class EmployeeAdmin(admin.ModelAdmin):
        list_display=('user','phonenumber', 'profile_picture')

class PsychologistAdmin(admin.ModelAdmin):
        list_display=('employee','bio')

admin.site.register(Client,ClientAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Psychologist,PsychologistAdmin)

class OutstandingTokenAdmin(token_blacklist.admin.OutstandingTokenAdmin):

    def has_delete_permission(self, *args, **kwargs):
        return True # or whatever logic you want

admin.site.unregister(token_blacklist.models.OutstandingToken)
admin.site.register(token_blacklist.models.OutstandingToken, OutstandingTokenAdmin)