from rest_framework import viewsets, mixins,permissions
from django.contrib.auth.models import User

from account.models import Psychologist,Employee,Client
from account.serializers import ClientSerializer
from .models import GoesTo, Schedule, Therapy, Fullcalendar
from .serializers import FullcalendarSerializer, PsychologistsClientsSerializer, ScheduleSerializer, TherapySerializer, GoesToSerializer
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


class PsychologistsTherapiesViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = TherapySerializer
    permision_classes = [IsPsychologistTherapyOwner]

    def get_queryset(self):
        return Therapy.objects.filter(psychologist_id=Psychologist.objects.get(employee=Employee.objects.get(user=self.request.user)).id)


class ClientViewPsychologistsTherapiesViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    serializer_class = TherapySerializer
    permision_classes = [permissions.IsAuthenticated,]

    def get_queryset(self):
        return Therapy.objects.filter(psychologist_id=GoesTo.objects.get(client=Client.objects.get(user=self.request.user)).psychologist_id,confirmation="confirmed")


class PsychologistsFullcalendarViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    serializer_class = FullcalendarSerializer
    permision_classes = [IsPsychologistTherapyOwner]

    def get_queryset(self):
        return Fullcalendar.objects.filter(psychologist_id=Psychologist.objects.get(employee=Employee.objects.get(user=self.request.user)).id,confirmation="confirmed")


class PsychologistsClientsViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    serializer_class = ClientSerializer
    permision_classes = [IsPsychologistTherapyOwner]

    def get_queryset(self):
        return Client.objects.filter(therapy__client_id__isnull=False, therapy__psychologist_id = Psychologist.objects.get(employee=Employee.objects.get(user=self.request.user)).id) #.values_list('user','phonenumber','birthdate')
        

class GoesToViewSet(mixins.CreateModelMixin, 
                    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
                    viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = GoesTo.objects.all()
    serializer_class = GoesToSerializer
    permission_classes=[permissions.AllowAny,]