from pydoc import cli
from django.contrib.auth.models import User,Group
from .models import GENDER_CHOICES, Client, Employee, Psychologist
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [ 'url','username','password','first_name','last_name','email']
        extra_kwargs = {
            'password': {'write_only': True},
            
        }
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super(UserSerializer, self).update(instance, validated_data)
    
    def login(self,validated_data):
        if User.objects.filter(username=validated_data['password']) is None:
            raise 

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    user=UserSerializer()
    class Meta:
        model = Client
        fields = ['id', 'user' ,'phonenumber','birthdate','gender']

    def create(self, validated_data):
        
        user_data=validated_data.pop('user')
       
        this_user=User.objects.create_user(**user_data)
        phonenumber=""
        if 'phonenumber' in validated_data:
                phonenumber=validated_data.pop('phonenumber')
        birthdate=""
        if 'birthdate' in validated_data:
                birthdate=validated_data.pop('birthdate')
        gender=""
        if 'gender' in validated_data:
                gender=validated_data.pop('gender')
        client_data={
            "user": user_data,
            "phonenumber": phonenumber,
            "birthdate": birthdate,
            "gender": gender
        }
        new_client=Client(user=this_user,phonenumber=client_data['phonenumber'],birthdate=client_data['birthdate'],gender=client_data['gender'])
        new_client.save()
        return new_client



class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    user=UserSerializer()
    class Meta:
        model = Employee
        fields = ['id', 'user' ,'phonenumber','profile_picture']
    
    def create(self, validated_data):
        user_data=validated_data.pop('user')
        this_user=User.objects.create_user(**user_data)
        phonenumber=""
        if 'phonenumber' in validated_data:
                phonenumber=validated_data.pop('phonenumber')
        profile_picture=""
        if 'profile_picture' in validated_data:
                profile_picture=validated_data.pop('profile_picture')
        employee_data={
            "user": user_data,
            "phonenumber": phonenumber,
            "profile_picture": profile_picture
        }
        new_employee=Employee(user=this_user,phonenumber=employee_data['phonenumber'],profile_picture=employee_data['profile_picture'])
        new_employee.save()
        return new_employee


class PsychologistSerializer(serializers.HyperlinkedModelSerializer):
    employee=EmployeeSerializer()
    class Meta:
        model = Psychologist
        fields = ['id', 'employee' ,'bio']
    
    def create(self, validated_data):
        employee_data=validated_data.pop('employee')
        user_data=employee_data.pop('user')
        this_user=User.objects.create_user(**user_data)
        new_employee=Employee(user=this_user,phonenumber=employee_data['phonenumber'],profile_picture=employee_data['profile_picture'])
        new_employee.save()
        if 'bio' in validated_data:
                bio=validated_data.pop('bio')
        psychologist_data={
            "bio": bio
        }
        new_psychologist=Psychologist(employee=new_employee,bio=psychologist_data['bio'])
        new_psychologist.save()
        return new_psychologist


