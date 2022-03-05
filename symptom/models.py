from django.db import models

from account.models import Client, Psychologist


class Symptom(models.Model):
    name = models.CharField(max_length=50, default="")


class PsychologicalDisorder(models.Model):
    name = models.CharField(max_length=50, default="")


class Feel(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("client", "symptom"),)


class CharacterizedBy(models.Model):
    psychological_disorder = models.ForeignKey(
        PsychologicalDisorder, on_delete=models.CASCADE
    )
    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("psychological_disorder", "symptom"),)


class FieldOfExpertise(models.Model):
    psychologist = models.ForeignKey(Psychologist, on_delete=models.CASCADE)
    psychological_disorder = models.ForeignKey(
        PsychologicalDisorder, on_delete=models.CASCADE
    )

    class Meta:
        unique_together = (("psychologist", "psychological_disorder"),)
