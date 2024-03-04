from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.validators import MaxValueValidator


class UserModelManager(BaseUserManager):
    def create_user(self, email, username,  password=None, **kwargs):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        email = email.lower()

        if not username:
            # if USERNAME is not entered, generate by EMAIL USERNAME
            username = email.split('@')[0]
        print("user.model.py - USERNAME: ", username)

        #?: Add Validation for fields

        user = self.model(
            email=email,
            **kwargs,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class UserModel(AbstractBaseUser, PermissionsMixin):
    USER_ROLE = 'user'
    ORGANISER_ROLE = 'organiser'
    ADMIN = "admin"  # admins are developers

    ROLE_CHOICES = [
        (USER_ROLE, 'User'),
        (ORGANISER_ROLE, 'Organiser'),
        (ADMIN, 'Admin')
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(unique=True, max_length=16)
    email = models.EmailField(unique=True, max_length=255)
    role = models.CharField(
        max_length=20, choices=ROLE_CHOICES, default=USER_ROLE)
    avatar_url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    forgot_pass_otp = models.IntegerField(blank=True, null=True, validators=[MaxValueValidator(999999)])
    forgot_pass_otp_expiry = models.DateTimeField(blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    objects = UserModelManager()

    def __str__(self):
        return self.username


