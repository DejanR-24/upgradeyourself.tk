from django.contrib.auth import get_user_model
from django.contrib.auth.models import User,Group
from .models import GENDER_CHOICES, Client,Employee,Psychologist
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [ 'username', 'first_name','last_name','email']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super(UserSerializer, self).update(instance, validated_data)

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    user=UserSerializer()
    class Meta:
        model = Client
        fields = ['id', 'user' ,'phonenumber','birthdate','gender']

    def to_representation(self, obj):
        """Move fields from user to user representation."""
        representation = super().to_representation(obj)
        user_representation = representation.pop('user')
        for key in user_representation:
            representation[key] = user_representation[key]
        return representation

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    user=UserSerializer()
    class Meta:
        model = Employee
        fields = ['id', 'user' ,'phonenumber','profile_picture']

    def to_representation(self, obj):
        """Move fields from user to user representation."""
        representation = super().to_representation(obj)
        user_representation = representation.pop('user')
        for key in user_representation:
            representation[key] = user_representation[key]
        return representation

class PsychologistSerializer(serializers.HyperlinkedModelSerializer):
    employee=EmployeeSerializer()
    class Meta:
        model = Psychologist
        fields = ['id', 'employee' ,'bio']

    def to_representation(self, obj):
        """Move fields from employee to Psychologist representation."""
        representation = super().to_representation(obj)
        employee_representation = representation.pop('employee')
        for key in employee_representation:
            representation[key] = employee_representation[key]
        return representation


