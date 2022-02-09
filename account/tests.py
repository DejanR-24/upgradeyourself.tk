import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from .models import Client, Employee, Psychologist
from .serializers import UserSerializer, ClientSerializer, EmployeeSerializer, PsychologistSerializer

class RegistrationTestCase(APITestCase):
    def test_registration(self):
        data={"username": "testcase", "email":"test@telekom.me",
               "password":"test2412","password2":"test2412"
               }
        response = self.client.post("http://127.0.0.1:8000/api/register/",data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)