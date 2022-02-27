from urllib import request
from django.db import models

from account.models import *


class WorkingHours(models.Model):
    time = models.TimeField(unique=True)

class ConfirmationStatus(models.Model):
    status = models.CharField(max_length=30,unique="True")

class Fullcalendar(models.Model):
    title = models.CharField(max_length=50)
    start = models.CharField(max_length=20)
    end = models.CharField(max_length=50)
    psychologist_id = models.ForeignKey(Psychologist,on_delete=models.CASCADE)
    confirmation_id = models.ForeignKey(ConfirmationStatus,default=1,on_delete=models.CASCADE)


class TherapyManager(models.Manager):
    def create(self, **obj_data):
        title = obj_data['client_id'].user.first_name + " " + obj_data['client_id'].user.last_name
        start = str(obj_data['date']) + "T" + str(obj_data['workinghours_id'].time)
        end_time = str(WorkingHours.objects.get(id=(obj_data['workinghours_id'].id+1)).time) if obj_data['workinghours_id'].id<8 else "20:00:00" #checking if this is the last working hour
        end = str(obj_data['date']) + "T" + end_time
        psychologist_id=obj_data['psychologist_id']
        confirmation_id=obj_data['confirmation_id']
        temp = Fullcalendar(title=title, start=start, end=end, psychologist_id=psychologist_id, confirmation_id=confirmation_id)
        temp.save()
        return super().create(**obj_data) 

    def update(self, instance,**obj_data):
        title = instance.client_id.user.first_name + " " + instance.client_id.user.last_name
        start = str(instance.date) + "T" + str(instance.WorkingHours_id.time)
        psychologist_id=obj_data['psychologist_id']
        temp = Fullcalendar.objects.get(title=title, start=start, psychologist_id=psychologist_id)
        temp.confirmation_id=obj_data['confirmation_id']
        temp.save()
        instance.confirmation_id = obj_data['confirmation_id']
        instance.save()
        return instance


class Therapy(models.Model):
    date = models.DateField()
    workinghours_id = models.ForeignKey(WorkingHours,on_delete=models.CASCADE)
    psychologist_id = models.ForeignKey(Psychologist,to_field='id',on_delete=models.CASCADE)
    client_id = models.ForeignKey(Client,to_field='id', on_delete=models.CASCADE)
    confirmation_id = models.ForeignKey(ConfirmationStatus,default=1,on_delete=models.CASCADE)

    objects = TherapyManager()




class GoesTo(models.Model):
    client = models.OneToOneField(Client,to_field='id',on_delete=models.CASCADE)
    psychologist_id = models.ForeignKey(Psychologist,to_field='id',on_delete=models.CASCADE)