# tests.py
from django.test import TestCase
from requests import Response
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework.authtoken.models import Token
from api.models import UserModel
from api.views import *

class UserViewsTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user_data = {
            "email": "test@example.com",
            "username": "test_user",
            "password": "test_password"
        }
        self.user = UserModel.objects.create_user(**self.user_data)
        self.token = Token.objects.create(user=self.user)

    def test_signup(self):
        signup_data ={
            "first_name": "John",
            "last_name": "Doe",
            "email": "newtest@example.com",
            "password": "test_password"
        }
        request = self.factory.post('/signup', signup_data, format='json')
        response = signup(request)
        self.assertEqual(response.status_code, 201)
        self.assertIn('token', response.data)
        self.assertIn('user', response.data)

    def test_login(self):
        request_data = {
            "username": self.user.username,
            "password": self.user_data['password']
        }
        request = self.factory.post('/login', request_data)
        response = login(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.data)
        self.assertIn('user', response.data)

    def test_change_password(self):
        new_password = "new_test_password"
        request_data = {
            "username": self.user.username,
            "current_password": self.user_data['password'],
            "new_password": new_password
        }
        request = self.factory.post('/change_password', request_data)
        force_authenticate(request, user=self.user)
        response = change_password(request)
        self.assertEqual(response.status_code, 200)
        user_updated = UserModel.objects.get(username=self.user.username)
        self.assertTrue(user_updated.check_password(new_password))
    def test_forgot_password(self):
        request_data = {"email": self.user_data['email']}
        request = self.factory.post('/forgot_password', request_data)
        response = forgot_password(request)
        self.assertEqual(response.status_code, 200)
        self.user.refresh_from_db()
        # The assertion might change based on how forgot_pass_otp is actually implemented
        self.assertTrue(UserModel.objects.get(email=self.user_data['email']).forgot_pass_otp is not None)

    def test_forgot_password_confirm(self):
        self.test_forgot_password() 
        self.user.refresh_from_db()
        otp = self.user.forgot_pass_otp
        new_password = "new_test_password"
        request_data = {
            "email": self.user_data['email'],
            "otp": otp,
            "new_password": new_password
        }
        request = self.factory.post('/forgot_password_confirm', request_data)
        response = forgot_password_confirm(request)
        self.assertEqual(response.status_code, 200)
        self.user.refresh_from_db()
        self.assertEqual(UserModel.objects.get(email=self.user_data['email']).check_password(new_password), True)

    def test_test_token(self):
        request = self.factory.get('/test_token')
        force_authenticate(request, user=self.user, token=self.token.key)
        response = test_token(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.data)
        self.assertEqual(response.data['message'], 'passed!')


# Create your tests here.