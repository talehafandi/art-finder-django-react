from django.test import TestCase
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.utils import timezone
from datetime import timedelta

class UserManagementTestCase(TestCase):
    def setUp(self):
        # Create a user for testing login and related functionalities
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword123')
        self.token, _ = Token.objects.get_or_create(user=self.user)
        self.client = APIClient()
    
    # Test cases for signup
    def test_signup(self):
        url = reverse('signup')  # Assuming you have a named URL for signup
        data = {'email': 'newuser@example.com', 'password': 'newuser123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_signup_with_invalid_email(self):
        url = reverse('signup')
        data = {'email': 'invalidemail', 'password': 'password123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Test cases for login
    def test_login(self):
        url = reverse('login')
        data = {'username': 'testuser', 'password': 'testpassword123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_login_with_wrong_password(self):
        url = reverse('login')
        data = {'username': 'testuser', 'password': 'wrongpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Test cases for changing password
    def test_change_password(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        url = reverse('change_password')
        data = {'username': 'testuser', 'current_password': 'testpassword123', 'new_password': 'newpassword123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_change_password_with_wrong_current_password(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        url = reverse('change_password')
        data = {'username': 'testuser', 'current_password': 'wrongpassword', 'new_password': 'newpassword456'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_authentication_required_for_changing_password(self):
        url = reverse('change_password')
        data = {'username': 'testuser', 'current_password': 'testpassword123', 'new_password': 'securepassword456'}
        response = self.client.post(url, data, format='json')  # No authentication provided
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)

    # Test cases for forgot password
    def test_forgot_password(self):
        url = reverse('forgot_password')
        data = {'email': 'test@example.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_forgot_password_for_nonexistent_email(self):
        url = reverse('forgot_password')
        data = {'email': 'nonexistent@example.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Test cases for forgot password confirm
    def test_forgot_password_confirm_with_expired_otp(self):
        # Setting up a user with an expired OTP
        user_with_expired_otp = User.objects.create_user(username='expiredotpuser', email='expiredotp@example.com', password='testpassword123')
        user_with_expired_otp.forgot_pass_otp = '123456'
        user_with_expired_otp.forgot_pass_otp_expiry = timezone.now() - timedelta(hours=1)  # Assuming the OTP expires after some time
        user_with_expired_otp.save()

        url = reverse('forgot_password_confirm')
        data = {'email': 'expiredotp@example.com', 'otp': '123456', 'new_password': 'newpassword789'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertIn('OTP is expired', response.data['message'])


# Create your tests here.