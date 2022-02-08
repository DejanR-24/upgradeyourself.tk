from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ClientSerializer, EmployeeSerializer, PsychologistSerializer, UserSerializer
from .models import Client, Employee, Psychologist

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]

class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Client.objects.all()#.order_by('-user.date_joined')
    serializer_class = ClientSerializer
    #permission_classes = [permissions.IsAuthenticated]

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Employee.objects.all()#.order_by('-user.date_joined')
    serializer_class = EmployeeSerializer
    #permission_classes = [permissions.IsAuthenticated]

class PsychologistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Psychologist.objects.all()#.order_by('-user.date_joined')
    serializer_class = PsychologistSerializer
    #permission_classes = [permissions.IsAuthenticated]
