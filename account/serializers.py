from django.contrib.auth.models import User,Group
from .models import GENDER_CHOICES, Client,Employee,Psychologist
from rest_framework import serializers



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'user' ,'phonenumber','birthdate','gender']

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'user' ,'phonenumber','profile_picture']

class PsychologistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Psychologist
        fields = ['id', 'employee' ,'bio']