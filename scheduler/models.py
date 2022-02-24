from ast import mod
from urllib import request
from django.db import models
from account.models import *


class Schedule(models.Model):
    time = models.TimeField(unique=True)


class Therapy(models.Model):
    date = models.DateField()
    shedule_id = models.ForeignKey(Schedule,on_delete=models.CASCADE)
    psychologist_id = models.ForeignKey(Psychologist,on_delete=models.CASCADE)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    

