from django.contrib import admin

from .models import (
    Symptom,
    PsychologicalDisorder,
    Feel,
    CharacterizedBy,
    FieldOfExpertise,
)


class SymptomAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class PsychologicalDisorderAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class FeelAdmin(admin.ModelAdmin):
    list_display = ("client", "symptom")


class CharacterizedByAdmin(admin.ModelAdmin):
    list_display = ("psychological_disorder", "symptom")


class FieldOfExpertiseAdmin(admin.ModelAdmin):
    list_display = ("psychologist", "psychological_disorder")


admin.site.register(Symptom, SymptomAdmin)
admin.site.register(PsychologicalDisorder, PsychologicalDisorderAdmin)
admin.site.register(Feel, FeelAdmin)
admin.site.register(CharacterizedBy, CharacterizedByAdmin)
admin.site.register(FieldOfExpertise, FieldOfExpertiseAdmin)
