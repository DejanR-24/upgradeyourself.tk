from django.contrib.auth.models import User
from rest_framework import viewsets, mixins, permissions, parsers


from .serializers import (
    UserSerializer,
    ClientSerializer,
    ClientProfileSerializer,
    EmployeeSerializer,
    EmployeeProfileSerializer,
    PsychologistSerializer,
    PsychologistProfileSerializer,
)
from .models import Client, Employee, Psychologist
from .permissions import (
    IsClientProfileOwner,
    IsEmployeeProfileOwner,
    IsPsychologistProfileOwner,
    IsSuperAdmin,
)


class UserViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows users to be viewed or edited by superuser.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        IsSuperAdmin,
    ]


class ClientViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows clients to be viewed or edited by superuser.
    """

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsSuperAdmin]


class ClientProfileViewSet(
    mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet
):
    """
    API endpoint that allows client to view or edit their profile.
    """

    serializer_class = ClientProfileSerializer
    permission_classes = [
        IsClientProfileOwner,
    ]

    def get_queryset(self):
        return Client.objects.filter(user=self.request.user)


class EmployeeViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows employees to be viewed or edited by superuser.
    """

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [
        IsSuperAdmin,
    ]


class EmployeeProfileViewSet(
    mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet
):
    """
    API endpoint that allows employees to view or edit their profile..
    """

    serializer_class = EmployeeProfileSerializer
    permission_classes = [
        IsEmployeeProfileOwner,
    ]

    def get_queryset(self):
        return Employee.objects.filter(user=self.request.user)


class PsychologistViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    """
    API endpoint that allows users to see Psychologists.
    """

    queryset = Psychologist.objects.all()
    serializer_class = PsychologistSerializer
    permission_classes = [permissions.AllowAny]


class PsychologistProfileViewSet(
    mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet
):
    """
    API endpoint that allows psychologists to view or edit their profile.
    """

    serializer_class = PsychologistProfileSerializer
    permission_classes = [
        IsPsychologistProfileOwner,
    ]

    def get_queryset(self):
        return Psychologist.objects.filter(
            employee=Employee.objects.get(user=self.request.user)
        )


class UploadProfilePictureViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows psychologists add a profile picture to employees.
    """
    permission_classes = (IsSuperAdmin,)
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.filter()
    parser_classes = (parsers.MultiPartParser, parsers.JSONParser)
