from rest_framework import mixins, viewsets, permissions

from account.permissions import IsSuperAdmin
from account.models import Psychologist, Employee, Client
from account.serializers import PsychologistProfileSerializer, PsychologistSerializer
from scheduler.models import GoesTo
from scheduler.permissions import IsPsychologistTherapyOwner, IsClientTherapyOwner
from .models import (
    Symptom,
    PsychologicalDisorder,
    Feel,
    FieldOfExpertise,
    CharacterizedBy,
)
from .serializers import (
    SymptomSerializer,
    PsychologicalDisorderSerializer,
    FeelSerializer,
    FieldOfExpertiseSerializer,
    CharacterizedBySerializer,
    PsychologistsClientsFeelSerializer,
)
from .algorithm import get_the_psychologist

class SymptomViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows SuperAdmin and Employees to work with symptoms.
    """

    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer
    permission_classes = [IsSuperAdmin, permissions.IsAdminUser]


class PsychologicalDisorderViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows SuperAdmin and Employees to work with psychological disorders.
    """

    queryset = PsychologicalDisorder.objects.all()
    serializer_class = PsychologicalDisorderSerializer
    permission_classes = [IsSuperAdmin, permissions.IsAdminUser]


class CharacterizedByViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows SuperAdmin and Employees to work with connection between symptoms and psichological disorders.
    """

    queryset = CharacterizedBy.objects.all()
    serializer_class = CharacterizedBySerializer
    permission_classes = [IsSuperAdmin, permissions.IsAdminUser]


class FeelViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows Client to see and manage symptoms that he feels.
    """

    serializer_class = FeelSerializer
    permission_classes = [IsClientTherapyOwner]

    def get_queryset(self):
        return Feel.objects.filter(client=Client.objects.get(user=self.request.user))


class FeelAdminViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows SuperAdmin to see conection between clients and symptoms.
    """

    queryset = Feel.objects.all()
    serializer_class = FeelSerializer
    permission_classes = [IsSuperAdmin]


class FieldOfExpertiseViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows SuperAdmin and Employees to work with conection between psychologists and symptoms.
    """

    serializer_class = FieldOfExpertiseSerializer
    permission_classes = [IsPsychologistTherapyOwner]

    def get_queryset(self):
        return FieldOfExpertise.objects.filter(
            psychologist=Psychologist.objects.get(
                employee=Employee.objects.get(user=self.request.user)
            )
        )


class FieldOfExpertiseAdminViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows SuperAdmin and Employees to work with conection between psychologists and symptoms.
    """

    queryset = FieldOfExpertise.objects.all()
    serializer_class = FieldOfExpertiseSerializer
    permission_classes = [IsSuperAdmin, permissions.IsAdminUser]


class FeelPsychologistsViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows SuperAdmin to see conection between clients and symptoms.
    """

    serializer_class = PsychologistsClientsFeelSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return Client.objects.values_list(
    'user_id',
    'feel__symptom' 
)
        
class ChoosePsychologistAlogrithmViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows SuperAdmin to see conection between clients and symptoms.
    """

    serializer_class = PsychologistSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Psychologist.objects.filter(id=get_the_psychologist(Client.objects.get(user=self.request.user)).id)