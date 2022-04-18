from email.policy import default
from unittest.util import _MAX_LENGTH
from rest_framework import serializers, status
from rest_framework.response import Response

from account.models import Client, Employee, Psychologist
from .models import (
    Symptom,
    PsychologicalDisorder,
    Feel,
    FieldOfExpertise,
    CharacterizedBy,
)


class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields = ("id", "name")


class PsychologicalDisorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PsychologicalDisorder
        fields = ("id", "name")


class FeelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feel
        fields = ("client", "symptom")
        extra_kwargs = {"client": {"read_only": True}}

    def create(self, validated_data):
        client = Client.objects.get(user=self.context["request"].user)
        symptom = Feel.objects.create(client=client, symptom=validated_data["symptom"])
        symptom.save()
        return symptom


class FieldOfExpertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldOfExpertise
        fields = ("psychologist", "psychological_disorder")
        extra_kwargs = {"psychologist": {"read_only": True}}

    def create(self, validated_data):
        if self.context["request"].user.is_superuser:
            FieldOfExpertise.objects.create(
                psychologist=validated_data["psychologist"],
                psichological_disorder=validated_data["psychological_disorder"],
            )
            field_of_expertise.save()
            return field_of_expertise

        psychologist = Psychologist.objects.get(
            employee=Employee.objects.get(user=self.context["request"].user)
        )
        field_of_expertise = FieldOfExpertise.objects.create(
            psychologist=psychologist,
            psichological_disorder=validated_data["psychological_disorder"],
        )
        field_of_expertise.save()
        return field_of_expertise


class CharacterizedBySerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterizedBy
        fields = ("symptom", "psychological_disorder")


class PsychologistsClientsFeelSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    symptom = serializers.CharField(max_length=50)
