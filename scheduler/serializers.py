from http import client
from importlib.metadata import requires
from re import I
from rest_framework import serializers,mixins
from django.contrib.auth.models import User

from .models import  ConfirmationStatus, WorkingHours, Therapy, GoesTo#,Fullcalendar
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
        client = Client.objects.get(user=self.context['request'].user).id
        psychologist = GoesTo.objects.get(client = Client.objects.get(user=self.context['request'].user).id).psychologist
        workinghours = WorkingHours.objects.get(time=validated_data['time'])
        confirmation = ConfirmationStatus.objects.get(id=1).id
        new_therapy=Therapy.objects.create(date=date,client=client,psychologist=psychologist,workinghours=workinghours,confirmation=confirmation)
        new_therapy.save()
        return new_therapy


class TherapySerializer(serializers.ModelSerializer):

    class Meta:
        model = Therapy
        fields = ('id','date','workinghours','psychologist','client','confirmation','title','start','end')
        extra_kwargs = {
            'title': {'read_only': True},
            'start': {'read_only': True},
            'end': {'read_only': True}
        }


    # def create(self, validated_data):
    #     date=validated_data['date']
    #     client = Client.objects.get(user=self.context['request'].user).id
    #     psychologist = GoesTo.objects.get(client = Client.objects.get(user=self.context['request'].user)).psychologist
    #     workinghours = WorkingHours.objects.get(time=validated_data['time']).id
    #     confirmation = 1
    #     new_therapy=Therapy(date=date,client=client,psychologist=psychologist,workinghours=workinghours,confirmation=confirmation)
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
        model = Therapy
        fields = ('title','start','end')


class GoesToSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoesTo
        fields = ('client','psychologist')
        extra_kwargs = {
            'client': {'read_only': True}
        }

    def create(self,validated_data):
        client = Client.objects.get(user=self.context['request'].user)
        goes_to = GoesTo.objects.create(
            client = client,
            psychologist=validated_data['psychologist']
        )
        goes_to.save()
        return goes_to

    def update(self, instance, validated_data):
        instance.psychologist=validated_data.get('psychologist', instance.psychologist)
        instance.save()
        return instance