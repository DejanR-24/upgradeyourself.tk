import datetime
from rest_framework import viewsets, mixins,permissions
from django.contrib.auth.models import User

from account.models import Psychologist,Employee,Client
from account.serializers import ClientSerializer
from account.permissions import IsSuperAdmin
from .models import GoesTo, WorkingHours, Therapy
from .serializers import  *
from .permissions import IsClientTherapyOwner, IsPsychologistTherapyOwner


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

# class PsychologistsTherapiesConfirmedViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
#     """
#     API endpoint that allows psychologist to see their scheduled therapies.
#     """
#     serializer_class = TherapySerializer
#     permission_classes = [IsPsychologistTherapyOwner]

#     def get_queryset(self):
#         return Therapy.objects.filter(psychologist=Psychologist.objects.get(employee=Employee.objects.get(user=self.request.user)),confirmation__id=2,date__gte = datetime.date.today(),date__lte = datetime.date.today() + datetime.timedelta(days=7)).order_by('date')


class PsychologistsTherapiesPendingViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows psychologist to see pending requests for therapies from clients.
    """
    serializer_class = TherapySerializer
    permission_classes = [IsPsychologistTherapyOwner]

    def get_queryset(self):
        return Therapy.objects.filter(psychologist=Psychologist.objects.get(employee=Employee.objects.get(user=self.request.user)),confirmation__id=1)


class ClientViewPsychologistsFullcalendarViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    API endpoint that converts result of confirmed therpies of the client's psychologist to fullcalendar format so that we can use their plugin.
    """
    serializer_class = ClientFullcalendarSerializer
    permission_classes = [IsClientTherapyOwner]

    def get_queryset(self):
        return Therapy.objects.filter(psychologist=GoesTo.objects.get(client=Client.objects.get(user=self.request.user)).psychologist,confirmation=2,date__gte = datetime.date.today(),date__lte = datetime.date.today() + datetime.timedelta(days=7)).order_by('date')


class PsychologistsTherapiesConfirmedViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    API endpoint that  allows psychologist to see his confirmed schedule.
    """
    serializer_class = PsychologistFullcalendarSerializer
    permission_classes = [IsPsychologistTherapyOwner]

    def get_queryset(self):
        return Therapy.objects.filter(psychologist=Psychologist.objects.get(employee=Employee.objects.get(user=self.request.user)).id,confirmation=2,date__gte = datetime.date.today(),date__lte = datetime.date.today() + datetime.timedelta(days=7)).order_by('date')


class ClientViewPsychologistsFullcalendarViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    API endpoint that  allows psychologist to see his confirmed schedule.
    """
    serializer_class = ClientFullcalendarSerializer
    permission_classes = [IsClientTherapyOwner]

    def get_queryset(self):
        return Therapy.objects.filter(psychologist=GoesTo.objects.get(client=Client.objects.get(user=self.request.user)).psychologist,confirmation=2)



class PsychologistsClientsViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    API endpoint that allows psychologist to see list of their clients.
    """
    serializer_class = ClientSerializer
    permission_classes = [IsPsychologistTherapyOwner]

    def get_queryset(self):
        return Client.objects.filter(goesto__client__isnull=False, goesto__psychologist = Psychologist.objects.get(employee=Employee.objects.get(user=self.request.user))) 
        

