from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import ConfirmationStatus, WorkingHours, Therapy, GoesTo
from account.models import Client
from my_auth.utils import Util


class WorkingHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingHours
        fields = ("id", "time")


class ConfirmationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfirmationStatus
        fields = ("id", "status")


class TherapyCreateSerializer(serializers.ModelSerializer):
    date = serializers.DateField(required=True)
    time = serializers.TimeField(required=True, write_only=True)

    class Meta:
        model = Therapy
        fields = ("date", "time")

    def create(self, validated_data):
        date = validated_data["date"]
        client = Client.objects.get(user=self.context["request"].user).id
        psychologist = GoesTo.objects.get(
            client=Client.objects.get(user=self.context["request"].user).id
        ).psychologist
        workinghours = WorkingHours.objects.get(time=validated_data["time"])
        confirmation = ConfirmationStatus.objects.get(id=1).id
        new_therapy = Therapy.objects.create(
            date=date,
            client=client,
            psychologist=psychologist,
            workinghours=workinghours,
            confirmation=confirmation,
        )
        new_therapy.save()
        return new_therapy


class TherapySerializer(serializers.ModelSerializer):
    class Meta:
        model = Therapy
        fields = (
            "id",
            "date",
            "workinghours",
            "psychologist",
            "client",
            "confirmation",
            "title",
            "start",
            "end",
        )
        extra_kwargs = {
            "title": {"read_only": True},
            "start": {"read_only": True},
            "end": {"read_only": True},
        }

    def update(self, instance, validated_data):
        if instance.confirmation != validated_data["confirmation"]:
            client = instance.client
            if validated_data["confirmation"] == ConfirmationStatus.objects.get(id=2):
                email_subject = (
                    "Response for therapy request on "
                    + str(instance.date)
                    + " at "
                    + str(instance.workinghours.time)
                )
                email_body = (
                    "Dear "
                    + client.user.first_name
                    + ",\n\nWe are happy to inform you that your therapy appointment is confirmed. We are grateful to you for using our services. \n\nAll the best,\n UpgradeYourself Team"
                )
                send_to = client.user.email
                data = {
                    "email_body": email_body,
                    "send_to": send_to,
                    "email_subject": email_subject,
                }
                Util.send_email(data)
                instance.confirmation = validated_data["confirmation"]
                instance.save()
                return instance
            else:
                email_subject = (
                    "Response for therapy request on "
                    + str(instance.date)
                    + " at "
                    + str(instance.workinghours.time)
                )
                email_body = (
                    "Dear "
                    + client.user.first_name
                    + ",\n\nWe are so sorry, but your psychologist has to reschedule therapy appointment, please visit our site to make a new request. We are grateful to you for using our services.\n\nAll the best,\n UpgradeYourself Team"
                )
                send_to = client.user.email
                data = {
                    "email_body": email_body,
                    "send_to": send_to,
                    "email_subject": email_subject,
                }
                Util.send_email(data)
                instance.delete()


class PsychologistFullcalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Therapy
        fields = ("title", "start", "end")


class ClientFullcalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Therapy
        fields = ("title", "start", "end")

    def to_representation(self, obj):
        data = super().to_representation(obj)
        data["title"] = "busy"
        return data


class GoesToSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoesTo
        fields = ("client", "psychologist")
        extra_kwargs = {"client": {"read_only": True}}

    def create(self, validated_data):
        client = Client.objects.get(user=self.context["request"].user)
        goes_to = GoesTo.objects.create(
            client=client, psychologist=validated_data["psychologist"]
        )
        goes_to.save()
        return goes_to

    def update(self, instance, validated_data):
        instance.psychologist = validated_data.get(
            "psychologist", instance.psychologist
        )
        instance.save()
        return instance
