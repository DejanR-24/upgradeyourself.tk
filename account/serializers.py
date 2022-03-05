from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import Client, Employee, Psychologist


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    is_staff = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(default=False)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "password",
            "password2",
            "email",
            "first_name",
            "last_name",
            "is_staff",
            "is_superuser",
        )
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
            "id": {"read_only": True},
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            is_staff=validated_data["is_staff"],
            is_superuser=validated_data["is_superuser"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    gender = serializers.IntegerField(default=0)

    class Meta:
        model = Client
        fields = ("id", "user", "phonenumber", "birthdate", "gender", "is_verified")
        extra_kwargs = {
            "is_verified": {"read_only": True},
        }

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        this_user = User.objects.create(
            username=user_data["username"],
            email=user_data["email"],
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            is_staff=False,
            is_superuser=False,
        )
        this_user.set_password(user_data["password"])
        this_user.save()
        new_client = Client(
            user=this_user,
            phonenumber=validated_data["phonenumber"],
            birthdate=validated_data["birthdate"],
            gender=validated_data["gender"],
            is_verified=False,
        )
        new_client.save()
        return new_client


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Employee
        fields = ("user", "phonenumber", "profile_picture")

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        this_user = User.objects.create(
            username=user_data["username"],
            email=user_data["email"],
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            is_staff=True,
            is_superuser=False,
        )
        this_user.set_password(user_data["password"])
        this_user.save()
        new_employee = Employee(
            user=this_user,
            phonenumber=validated_data["phonenumber"],
            profile_picture=validated_data["profile_picture"],
        )
        new_employee.save()
        return new_employee


class PsychologistSerializer(serializers.HyperlinkedModelSerializer):
    employee = EmployeeSerializer()

    class Meta:
        model = Psychologist
        fields = ("id", "employee", "bio")

    def create(self, validated_data):
        user_data = validated_data["employee"].pop("user")
        this_user = User.objects.create(
            username=user_data["username"],
            email=user_data["email"],
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            is_staff=True,
            is_superuser=True,
        )
        this_user.set_password(user_data["password"])
        this_user.save()
        new_employee = Employee(
            user=this_user,
            phonenumber=validated_data["employee"]["phonenumber"],
            profile_picture=validated_data["employee"]["profile_picture"],
        )
        new_employee.save()
        new_psychologist = Psychologist(
            employee=new_employee, bio=validated_data["bio"]
        )
        new_psychologist.save()
        return new_psychologist


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name")
        extra_kwargs = {
            "id": {"read_only": True},
            "username": {"read_only": True},
            "email": {"read_only": True},
        }


class ClientProfileSerializer(serializers.ModelSerializer):
    user = UpdateUserSerializer()
    gender = serializers.IntegerField(default=0)

    class Meta:
        model = Client
        fields = ("id", "user", "phonenumber", "birthdate", "gender", "is_verified")
        extra_kwargs = {
            "is_verified": {"read_only": True},
        }

    def update(self, instance, validated_data):
        user_data = validated_data["user"]
        user = User.objects.get(id=instance.user.id)
        user.first_name = user_data.get("first_name", user.first_name)
        user.last_name = user_data.get("last_name", user.last_name)
        user.save()
        instance.phonenumber = validated_data.get("phonenumber", instance.phonenumber)
        instance.birthdate = validated_data.get("birthdate", instance.birthdate)
        instance.save()
        return instance


class EmployeeProfileSerializer(serializers.ModelSerializer):
    user = UpdateUserSerializer()

    class Meta:
        model = Employee
        fields = ("id", "user", "phonenumber", "profile_picture")

    def update(self, instance, validated_data):
        user_data = validated_data["user"]
        user = User.objects.get(id=instance.user.id)
        user.first_name = user_data.get("first_name", user.first_name)
        user.last_name = user_data.get("last_name", user.last_name)
        user.save()
        instance.phonenumber = validated_data.get("phonenumber", instance.phonenumber)
        instance.profile_picture = validated_data.get(
            "profile_picture", instance.profile_picture
        )
        instance.save()
        return instance


class PsychologistProfileSerializer(serializers.ModelSerializer):
    employee = EmployeeProfileSerializer()

    class Meta:
        model = Psychologist
        fields = ("id", "employee", "bio")

    def update(self, instance, validated_data):
        user_data = validated_data["employee"]["user"]
        user = User.objects.get(id=instance.employee.user.id)
        user.first_name = user_data.get("first_name", user.first_name)
        user.last_name = user_data.get("last_name", user.last_name)
        user.save()
        employee_data = validated_data["employee"]
        employee = Employee.objects.get(id=instance.employee.id)
        employee.phonenumber = employee_data.get("phonenumber", employee.phonenumber)
        employee.profile_picture = employee_data.get(
            "profile_picture", employee.profile_picture
        )
        employee.save()
        instance.bio = validated_data.get("bio", instance.bio)
        instance.save()
        return instance
