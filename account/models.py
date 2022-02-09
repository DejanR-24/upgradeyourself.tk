from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = (
    (0, 'not specified'),
    (1, 'male'),
    (2, 'female'),
    (3, 'other'),
)

class Client(models.Model):
   user = models.OneToOneField(User, unique=True,on_delete=models.CASCADE)
   phonenumber = models.CharField(max_length=10,verbose_name="phone number")
   birthdate = models.DateField(verbose_name="birth date")
   gender= models.IntegerField(choices=GENDER_CHOICES, default=0)




class Employee(models.Model):
   user = models.OneToOneField(User, unique = True, on_delete=models.CASCADE)
   phonenumber = models.CharField(max_length=10,verbose_name="phone number")
   profile_picture = models.URLField(default="")

class Psychologist(models.Model):
   employee = models.OneToOneField(Employee,unique=True, on_delete=models.CASCADE)
   bio = models.TextField(max_length=1500)


   


