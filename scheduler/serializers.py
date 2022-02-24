from rest_framework import serializers,mixins
from django.contrib.auth.models import User

from .models import Schedule, Therapy
from account.models import Client, Psychologist

class ScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schedule
        fields = ('id','time')

class TherapySerializer(serializers.ModelSerializer):

    class Meta:
        model = Therapy
        fields = ('date','shedule_id','psychologist_id','client_id')





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


# class TrackListingField(serializers.RelatedField):
#     def to_representation(self, value):
#         duration = time.strftime('%M:%S', time.gmtime(value.duration))
#         return 'Track %d: %s (%s)' % (value.order, value.name, duration)

# class AlbumSerializer(serializers.ModelSerializer):
#     tracks = TrackListingField(many=True)

#     class Meta:
#         model = Album
#         fields = ['album_name', 'artist', 'tracks']
