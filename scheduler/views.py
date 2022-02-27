import datetime
#from datetime import timedelta, date
from rest_framework import viewsets, mixins,permissions
from django.contrib.auth.models import User

from account.models import Psychologist,Employee,Client
from account.serializers import ClientSerializer
from account.permissions import IsSuperAdmin
from .models import GoesTo, WorkingHours, Therapy, Fullcalendar
from .serializers import FullcalendarSerializer, TherapyCreateSerializer ,PsychologistsClientsSerializer, WorkingHoursSerializer, TherapySerializer, GoesToSerializer
from .permissions import IsPsychologistTherapyOwner


class WorkingHoursViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, 
                    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
                    viewsets.GenericViewSet):
    """
    API endpoint that allows SuperAdmin to work with working hours.
    """
    queryset = WorkingHours.objects.all()
    serializer_class = WorkingHoursSerializer
    permission_classes=[IsSuperAdmin,]


class TherapyViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, 
                    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
                    viewsets.GenericViewSet):
    """
    API endpoint that allows SuperAdmin to see and work with therapies.
    """
    queryset = Therapy.objects.all()
    serializer_class = TherapySerializer
    permission_classes=[permissions.AllowAny]


class ScheduleTherapyViewSet(mixins.CreateModelMixin,  
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    """
    API endpoint that allows clients to schedule a therapy with their chosen psychologist.
    """
    queryset = Therapy.objects.all()
    serializer_class = TherapyCreateSerializer 
    permission_classes=[permissions.IsAuthenticated]
   
class GoesToViewSet(mixins.CreateModelMixin, 
                    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
                    viewsets.GenericViewSet):
    """
    API endpoint that allows clients to be choose their psychologist.
    """
    queryset = GoesTo.objects.all()
    serializer_class = GoesToSerializer
    permission_classes=[permissions.AllowAny,]

class PsychologistsTherapiesConfirmedViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows psychologist to see their scheduled therapies.
    """
    serializer_class = TherapySerializer
    permision_classes = [IsPsychologistTherapyOwner]

    def get_queryset(self):
        return Therapy.objects.filter(psychologist_id=Psychologist.objects.get(employee=Employee.objects.get(user=self.request.user)).id,confirmation_id=2,date__gte = datetime.date.today(),date__lte = datetime.date.today() + datetime.timedelta(days=7)).order_by('date')


class PsychologistsTherapiesPendingViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows psychologist to see pending requests for therapies from clients.
    """
    serializer_class = TherapySerializer
    permision_classes = [IsPsychologistTherapyOwner]

    def get_queryset(self):
        return Therapy.objects.filter(psychologist_id=Psychologist.objects.get(employee=Employee.objects.get(user=self.request.user)).id,confirmation_id=1)

class ClientViewPsychologistsTherapiesViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    API endpoint that allows clients to see schedule of their chosen psychologists.
    """
    serializer_class = TherapySerializer
    permision_classes = [permissions.IsAuthenticated,]

    def get_queryset(self):
        return Therapy.objects.filter(psychologist_id=GoesTo.objects.get(client=Client.objects.get(user=self.request.user)).psychologist_id,confirmation_id=2)


class PsychologistsFullcalendarViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    API endpoint that converts result of confirmed therpies of the client's psychologist to fullcalendar format so that we can use their plugin.
    """
    serializer_class = FullcalendarSerializer
    permision_classes = [IsPsychologistTherapyOwner]

    def get_queryset(self):
        return Fullcalendar.objects.filter(psychologist_id=GoesTo.objects.get(client_id=Client.objects.get(user=self.request.user)).psychologist_id,confirmation_id=2,date__gte = datetime.date.today(),date__lte =datetime.date.today() + datetime.timedelta(days=7))


class PsychologistsClientsViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    API endpoint that allows psychologist to see list of their clients.
    """
    serializer_class = ClientSerializer
    permision_classes = [IsPsychologistTherapyOwner]

    def get_queryset(self):
        return Client.objects.filter(goesto__client__isnull=False, goesto__psychologist_id = Psychologist.objects.get(employee=Employee.objects.get(user=self.request.user)).id) 
        

