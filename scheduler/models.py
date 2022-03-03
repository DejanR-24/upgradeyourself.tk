from urllib import request
from django.db import models

from account.models import *


class WorkingHours(models.Model):
    time = models.TimeField(unique=True)

class ConfirmationStatus(models.Model):
    status = models.CharField(max_length=30,unique="True")

# class Fullcalendar(models.Model):
#     title = models.CharField(max_length=50)
#     start = models.CharField(max_length=20)
#     end = models.CharField(max_length=50)
#     psychologist = models.ForeignKey(Psychologist,to_field='id',on_delete=models.CASCADE)
#     confirmation = models.ForeignKey(ConfirmationStatus,to_field='id',default=1,on_delete=models.CASCADE)


class TherapyManager(models.Manager):
    def create(self, **obj_data):
        this_client = Client.objects.get(id=obj_data['client'])
        obj_data['client']=Client.objects.get(id=obj_data['client'])
        obj_data['confirmation']=ConfirmationStatus.objects.get(id=1)
        title = this_client.user.first_name + " " + this_client.user.last_name
        #start = str(obj_data['date']) + "T" + str(WorkingHours.objects.get(id=obj_data['workinghours']).time)
        #end_time = str(WorkingHours.objects.get(id=(obj_data['workinghours']+1)).time) if obj_data['workinghours']<8 else "20:00:00" #checking if this is the last working hour
        start = str(obj_data['date']) + "T" + str(obj_data['workinghours'].time)
        end_time = str(WorkingHours.objects.get(id=(obj_data['workinghours'].id+1)).time) if obj_data['workinghours'].id<8 else "20:00:00" #checking if this is the last working hour
        
        end = str(obj_data['date']) + "T" + end_time
        obj_data['title']=title
        obj_data['start']=start
        obj_data['end']=end
        return super().create(**obj_data) 




class Therapy(models.Model):
    date = models.DateField()
    workinghours = models.ForeignKey(WorkingHours,on_delete=models.CASCADE)
    psychologist = models.ForeignKey(Psychologist,on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    confirmation = models.ForeignKey(ConfirmationStatus,on_delete=models.CASCADE)
    title = models.CharField(max_length=50, default="")
    start = models.CharField(max_length=20,default="")
    end = models.CharField(max_length=50,default="")

    objects = TherapyManager()
    class Meta:
        unique_together = (("date", "workinghours","psychologist"),)


class GoesTo(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    psychologist = models.ForeignKey(Psychologist,on_delete=models.CASCADE)

    class Meta:
        unique_together = (("client", "psychologist"),)