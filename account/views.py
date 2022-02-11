from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.permissions import AllowAny
from rest_framework import mixins
from rest_framework import generics

from .serializers import UserSerializer, ClientSerializer, EmployeeSerializer, PsychologistSerializer
from .models import Client, Employee, Psychologist


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
#    permission_classes = [permissions.IsAdminUser]

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (AllowAny,)

        return super(UserViewSet, self).get_permissions()



class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Client.objects.all()#.order_by('-user.date_joined')
    serializer_class = ClientSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (AllowAny,)

        return super(ClientViewSet, self).get_permissions()


class EmployeeViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, 
                    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
                    viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Employee.objects.all()#.order_by('-user.date_joined')
    serializer_class = EmployeeSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (AllowAny,)

        return super(EmployeeViewSet, self).get_permissions()


class PsychologistViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, 
                    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
                    viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Psychologist.objects.all()#.order_by('-user.date_joined')
    serializer_class = PsychologistSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (AllowAny,)

        return super(PsychologistViewSet, self).get_permissions()