from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from account.models import Client, Employee, Psychologist


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token





class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ClientSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    gender= serializers.IntegerField(default=0)
    class Meta:
        model = Client
        fields = ('user', 'phonenumber','birthdate','gender')

    def create(self, validated_data):
        user_data=validated_data.pop('user')
        this_user = User.objects.create(
            username=user_data['username'],
            email=user_data['email'],
            first_name=user_data['first_name'],
            last_name=user_data['last_name']
        )
        this_user.set_password(user_data['password'])
        this_user.save()
        new_client=Client(user=this_user,phonenumber=validated_data['phonenumber'],birthdate=validated_data['birthdate'],gender=validated_data['gender'])
        new_client.save()
        return new_client

class EmployeeSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model = Employee
        fields = ('user', 'phonenumber','profile_picture')

    def create(self, validated_data):
        user_data=validated_data.pop('user')
        this_user = User.objects.create(
            username=user_data['username'],
            email=user_data['email'],
            first_name=user_data['first_name'],
            last_name=user_data['last_name']
        )
        this_user.set_password(user_data['password'])
        this_user.save()
        new_employee=Employee(user=this_user,phonenumber=validated_data['phonenumber'],profile_picture=validated_data['profile_picture'])
        new_employee.save()
        return new_employee

class PsychologistSerializer(serializers.ModelSerializer):
    employee=EmployeeSerializer()
    class Meta:
        model = Psychologist
        fields = ('employee', 'bio')

    def create(self, validated_data):
        user_data=validated_data['employee'].pop('user')
        this_user = User.objects.create(
            username=user_data['username'],
            email=user_data['email'],
            first_name=user_data['first_name'],
            last_name=user_data['last_name']
        )
        this_user.set_password(user_data['password'])
        this_user.save()
        new_employee=Employee(user=this_user,phonenumber=validated_data['employee']['phonenumber'],profile_picture=validated_data['employee']['profile_picture'])
        new_employee.save()
        new_psychologist=Psychologist(employee=new_employee,bio=validated_data['bio'])
        new_psychologist.save()
        return new_psychologist