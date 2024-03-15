# import boto3
import random
import requests
from urllib.parse import quote
# from datetime import datetime


import cloudinary
import cloudinary.uploader
# import cloudinary.api	

from decouple import config


cloudinary.config( 
  	cloud_name = config('CLOUDINARY_NAME'),
  	api_key = config('CLOUDINARY_KEY'),
  	api_secret = config('CLOUDINARY_SECRET')
)

def upload_file(file):
    result = cloudinary.uploader.upload(file)
    return result['secure_url'] # get file url

def generate_avatar(fullname):
    colors = ['f44336', 'e91e63', '9c27b0', '673ab7', '3f51b5', '2196f3', '03a9f4', '00bcd4',
            '009688', '4caf50', '8bc34a', 'cddc39', 'ffeb3b'] # background colors

    color = random.choice(colors)
    encoded_name = quote(fullname) # take first letter of full name
    avatar_url = f"https://ui-avatars.com/api/?background={color}&color=fff&name={encoded_name}" # generate url for api
    # filename = f"avatar-{datetime.today().microsecond}.png" # generate unique filename

    file = requests.get(avatar_url).content # get image
    avatar_url = upload_file(file) # upload to cloud

    return avatar_url

    # def generate_avatar_and_save(name, image):
    #     avatar = generate_avatar(name)
    #     return None

from django.conf import settings
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.backends import TokenBackend


class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        try: 
            header = self.get_header(request)
            if header is None: return None

            raw_token = self.get_raw_token(header)
            validated_token = self.get_validated_token(raw_token)
            print("val tok:", validated_token)

            return self.get_user(validated_token), validated_token
        except:
            return None

from django.template.loader import render_to_string, get_template
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives


def send_otp(receiver, otp):
    email_html = render_to_string('otp_email.html', {'otp': otp})

    msg = EmailMultiAlternatives(
        subject='Your OTP for Password Reset',
        body='Password Reset',
        from_email=settings.EMAIL_HOST_USER,
        to=[receiver]
    )

    msg.attach_alternative(email_html, "text/html")
    msg.send()