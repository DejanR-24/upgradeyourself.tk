from http import client
from importlib.metadata import requires
from re import I
from rest_framework import serializers,mixins
from django.contrib.auth.models import User

from .models import Fullcalendar, ConfirmationStatus, WorkingHours, Therapy, GoesTo
from account.models import Client, Psychologist

class WorkingHoursSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkingHours
        fields = ('id','time')

class ConfirmationStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConfirmationStatus
        fields = ('id','status')


class TherapyCreateSerializer(serializers.ModelSerializer):
    date=serializers.DateField(required=True)
    time=serializers.TimeField(required=True,write_only=True)

    class Meta:
        model = Therapy
        fields = ('date','time')

    def create(self, validated_data):
        date=validated_data['date']
        client_id = Client.objects.get(user=self.context['request'].user)
        psychologist_id = GoesTo.objects.get(client = Client.objects.get(user=self.context['request'].user)).psychologist_id
        workinghours_id = WorkingHours.objects.get(time=validated_data['time'])
        confirmation_id = ConfirmationStatus.objects.get(id=1)
        new_therapy=Therapy.objects.create(date=date,client_id=client_id,psychologist_id=psychologist_id,workinghours_id=workinghours_id,confirmation_id=confirmation_id)
        new_therapy.save()
        return new_therapy


class TherapySerializer(serializers.ModelSerializer):

    class Meta:
        model = Therapy
        fields = ('date','workinghours_id','psychologist_id','client_id','confirmation_id')

    # def create(self, validated_data):
    #     date=validated_data['date']
    #     client_id = Client.objects.get(user=self.context['request'].user).id
    #     psychologist_id = GoesTo.objects.get(client = Client.objects.get(user=self.context['request'].user)).psychologist_id
    #     workinghours_id = WorkingHours.objects.get(time=validated_data['time']).id
    #     confirmation_id = 1
    #     new_therapy=Therapy(date=date,client_id=client_id,psychologist_id=psychologist_id,workinghours_id=workinghours_id,confirmation_id=confirmation_id)
    #     new_therapy.save()
    #     return new_therapy


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']
    
from .mixins import FlattenMixin

class PsychologistsClientsSerializer(FlattenMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ('user', 'phonenumber', 'birthdate')
        flatten = [ ('user', UserSerializer) ]


class FullcalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fullcalendar
        fields = ('title','start','end')


class GoesToSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoesTo
        fields = ('client','psychologist_id')
        extra_kwargs = {
            'client': {'read_only': True}
        }

    def create(self,validated_data):
        client = Client.objects.get(user=self.context['request'].user)
        goes_to = GoesTo.objects.create(
            client = client,
            psychologist_id=validated_data['psychologist_id']
        )
        goes_to.save()
        return goes_to

    def update(self, instance, validated_data):
        instance.psychologist_id=validated_data.get('psychologist_id', instance.psychologist_id)
        instance.save()
        return instance