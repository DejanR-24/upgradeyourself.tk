import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
import json

from .models import Client, Employee, Psychologist
from .serializers import UserSerializer, ClientSerializer, EmployeeSerializer, PsychologistSerializer

class RegistrationTestCase(TestCase):
    def test_registration(self):
        json_data={
    "employee": {
        "user":{
            "username": "jelena",
            "password": "dejan2412",
            "first_name": "ivanovic",
            "last_name": "ivan",
            "email": "ivan@gmail.com"
        },
        "phonenumber": "3845345",
        "profile_picture": "https://trueorfalse.tk"
    },
    "bio": "Great expert"
    }
               
        response = self.client.post("http://127.0.0.1:8000/api/psychologists/",json.dumps(json_data),
                                content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)