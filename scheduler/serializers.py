from re import I
from rest_framework import serializers,mixins
from django.contrib.auth.models import User

from .models import Fullcalendar, Schedule, Therapy, GoesTo
from account.models import Client, Psychologist

class ScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schedule
        fields = ('id','time')

class TherapySerializer(serializers.ModelSerializer):

    class Meta:
        model = Therapy
        fields = ('date','schedule_id','psychologist_id','client_id','confirmation')

    # def create(self, validated_data):
    #     date=validated_data['date']
    #     client_id = Client.objects.get(user=self.context['request'].user).id
    #     psychologist_id = self.context['request'].id
    #     schedule_id = validated_data['schedule_id']
    #     confirmation= validated_data['confirmation']
    #     new_therapy=Therapy(employee=new_employee,bio=validated_data['bio'])
    #     new_psychologist.save()
    #     return new_psychologist


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