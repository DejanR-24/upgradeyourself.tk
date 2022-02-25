from ast import mod
from queue import Full
from urllib import request
from django.db import models

from account.models import *


class Schedule(models.Model):
    time = models.TimeField(unique=True)

class Fullcalendar(models.Model):
    title = models.CharField(max_length=50)
    start = models.CharField(max_length=20)
    end = models.CharField(max_length=50)
    psychologist_id = models.ForeignKey(Psychologist,on_delete=models.CASCADE)

class TherapyManager(models.Manager):

    def create(self, **obj_data):
        title = obj_data['client_id'].user.first_name + " " + obj_data['client_id'].user.last_name
        start = str(obj_data['date']) + "T" + str(obj_data['schedule_id'].time)
        end_time = str(Schedule.objects.get(id=(obj_data['schedule_id'].id+1)).time) if obj_data['schedule_id'].id<19 else "20:00:00" #checking if this is the last working hour
        end = str(obj_data['date']) + "T" + end_time
        psychologist_id=obj_data['psychologist_id']
        temp = Fullcalendar(title=title, start=start, end=end, psychologist_id=psychologist_id)
        temp.save()
        return super().create(**obj_data) 


class Therapy(models.Model):
    date = models.DateField()
    schedule_id = models.ForeignKey(Schedule,on_delete=models.CASCADE)
    psychologist_id = models.ForeignKey(Psychologist,to_field='id',on_delete=models.CASCADE)
    client_id = models.ForeignKey(Client,to_field='id', on_delete=models.CASCADE)
    
    objects = TherapyManager()

