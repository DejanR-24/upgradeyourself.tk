from base64 import b64encode
from django.contrib.auth.models import User
from rest_framework import viewsets, mixins,permissions, parsers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .serializers import UserSerializer, ClientSerializer, ClientProfileSerializer,  EmployeeSerializer, EmployeeProfileSerializer, PsychologistSerializer, PsychologistProfileSerializer
from .models import Client, Employee, Psychologist
from .permissions import IsClientProfileOwner, IsEmployeeProfileOwner, IsPsychologistProfileOwner, IsSuperAdmin

# CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class UserViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, 
                    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
                    viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes=[IsSuperAdmin,]


class ClientViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, 
                    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
                    viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes=[IsSuperAdmin,permissions.AllowAny]
    


class ClientProfileViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, 
                    viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = ClientProfileSerializer
    permission_classes=[IsClientProfileOwner,]
    
    def get_queryset(self):
        return Client.objects.filter(user=self.request.user)


class EmployeeViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, 
                    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
                    viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Employee.objects.all()#.order_by('-user.date_joined')
    serializer_class = EmployeeSerializer
    permission_classes=[IsSuperAdmin,]


class EmployeeProfileViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, 
                    viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = EmployeeProfileSerializer
    permission_classes=[IsEmployeeProfileOwner,]
    
    def get_queryset(self):
        return Employee.objects.filter(user=self.request.user)

# @cache_page(CACHE_TTL)
class PsychologistViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, 
                    viewsets.GenericViewSet):
    """
    API endpoint that allows users to see Psychologists.
    """
    queryset = Psychologist.objects.all()
    serializer_class = PsychologistSerializer
    permission_classes=[permissions.AllowAny]


class PsychologistProfileViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, 
                    viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = PsychologistProfileSerializer
    permission_classes=[IsPsychologistProfileOwner,]
    
    def get_queryset(self):
        return Psychologist.objects.filter(employee=Employee.objects.get(user=self.request.user))



class UploadProfilePictureViewSet(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    permission_classes = (IsSuperAdmin,)
    serializer_class = (EmployeeSerializer)
    queryset = Employee.objects.filter()
    parser_classes = (parsers.MultiPartParser,parsers.JSONParser)