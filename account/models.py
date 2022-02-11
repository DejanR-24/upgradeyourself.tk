from django.db import models
from django.contrib.auth.models import User


# Create your models here.

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

    # def create_client(self, user, phonenumber, birthdate, gender):
    #     """
    #     Create and save a user with the given username, email, and password.
    #     """
    #     if not user:
    #         raise ValueError('The given user must be set')
    #     self.phonenumber=phonenumber
    #     birthdate=birthdate
    #     gender=gender
    #     client = Client(username=username, email=email, **extra_fields)
    #     client.save(using=self._db)
    #     return client



class Employee(models.Model):
   user = models.OneToOneField(User, unique = True, on_delete=models.CASCADE)
   phonenumber = models.CharField(max_length=10,verbose_name="phone number")
   profile_picture = models.URLField(default="")

class Psychologist(models.Model):
   employee = models.OneToOneField(Employee,unique=True, on_delete=models.CASCADE)
   bio = models.TextField(max_length=1500)
