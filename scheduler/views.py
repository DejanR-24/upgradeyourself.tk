from rest_framework import viewsets, mixins,permissions
from django.contrib.auth.models import User

from account.models import Psychologist,Employee,Client
from account.serializers import ClientSerializer
from .models import Schedule, Therapy
from .serializers import PsychologistsClientsSerializer, ScheduleSerializer, TherapySerializer
from .permissions import IsPsychologistTherapyOwner

class ScheduleViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, 
                    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
                    viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes=[permissions.AllowAny,]

class TherapyViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, 
                    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
                    viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Therapy.objects.all()
    serializer_class = TherapySerializer
    permission_classes=[permissions.AllowAny]


class PsychologistsTherapiesViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    serializer_class = TherapySerializer
    permision_classes = [IsPsychologistTherapyOwner]

    def get_queryset(self):
        return Therapy.objects.filter(psychologist_id=Psychologist.objects.get(employee=Employee.objects.get(user=self.request.user)).id)

class PsychologistsClientsViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    serializer_class = ClientSerializer
    permision_classes = [IsPsychologistTherapyOwner]

    def get_queryset(self):
        return Client.objects.filter(therapy__client_id__isnull=False, therapy__psychologist_id = Psychologist.objects.get(employee=Employee.objects.get(user=self.request.user)).id) #.values_list('user','phonenumber','birthdate')
        
