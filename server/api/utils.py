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