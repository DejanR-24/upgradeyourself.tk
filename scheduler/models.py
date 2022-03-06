from django.db import models
from django.db import IntegrityError
from rest_framework import status
from rest_framework.response import Response

from account.models import Client, Psychologist


class WorkingHours(models.Model):
    time = models.TimeField(unique=True)


class ConfirmationStatus(models.Model):
    status = models.CharField(max_length=30, unique="True")


class TherapyManager(models.Manager):
    def create(self, **obj_data):
        this_client = Client.objects.get(id=obj_data["client"])
        obj_data["client"] = Client.objects.get(id=obj_data["client"])
        obj_data["confirmation"] = ConfirmationStatus.objects.get(id=1)
        title = this_client.user.first_name + " " + this_client.user.last_name
        start = str(obj_data["date"]) + "T" + str(obj_data["workinghours"].time)
        end_time = (
            str(WorkingHours.objects.get(id=(obj_data["workinghours"].id + 1)).time)
            if obj_data["workinghours"].id
            < 8  # checking if this is the last working hour
            else "20:00:00"
        )
        end = str(obj_data["date"]) + "T" + end_time
        obj_data["title"] = title
        obj_data["start"] = start
        obj_data["end"] = end
        return super().create(**obj_data)


class Therapy(models.Model):
    date = models.DateField()
    workinghours = models.ForeignKey(WorkingHours, on_delete=models.CASCADE)
    psychologist = models.ForeignKey(Psychologist, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    confirmation = models.ForeignKey(ConfirmationStatus, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, default="")
    start = models.CharField(max_length=20, default="")
    end = models.CharField(max_length=50, default="")

    objects = TherapyManager()

    class Meta:
        unique_together = (("date", "workinghours", "psychologist"),)


class GoesTo(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    psychologist = models.ForeignKey(Psychologist, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("client", "psychologist"),)

    def create(self, validated_data):
        client = validated_data["client"]
        try:
            goes_to = GoesTo(client=client, psychologist=validated_data["psychologist"])
            goes_to.save()
        except IntegrityError as e:
            return Response({"detail": "input is not valid"}, status=status.HTTP_400)
        return goes_to
