from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

GENDER_CHOICES = (
    (0, 'not specified'),
    (1, 'male'),
    (2, 'female'),
    (3, 'other'),
)

def upload_to(instance, filename):
    return 'profile_picture/{filename}'.format(filename=filename)



class Client(models.Model):
    user = models.OneToOneField(User, unique=True,on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=10,verbose_name="phone number")
    birthdate = models.DateField(verbose_name="birth date")
    gender= models.IntegerField(choices=GENDER_CHOICES, default=0)
    is_verified = models.BooleanField(default=False)

    def get_email(self):
        return self.user.email

    def get_user_id(self):
        return self.user.id

    def last_login(self):
        return self.user.last_login


class Employee(models.Model):
   user = models.OneToOneField(User, unique = True, on_delete=models.CASCADE)
   phonenumber = models.CharField(max_length=10,verbose_name="phone number")
   profile_picture = models.ImageField(_("Image"),upload_to=upload_to, default='profile_picetur/avatar.jpg')

class Psychologist(models.Model):
   employee = models.OneToOneField(Employee,unique=True, on_delete=models.CASCADE)
   bio = models.TextField(max_length=1500)


