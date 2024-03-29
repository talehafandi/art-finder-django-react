from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# VENUE MODEL
class VenueModel(models.Model):
    MAX_NAME_LENGTH = 32
    MAX_DESCRIPTION_LENGTH = 200
    MAX_ADDRESS_LENGTH = 40
    MAX_URL_LENGTH = 200

    # Enum for the event types
    MUSEUM = "MU"
    GALLERY = "GA"

    VENUE_CATEGORY_CHOICES = [
        (MUSEUM, "MUSEUM"),
        (GALLERY, "GALLERY"),
    ]

    # Event model fields
    name = models.CharField(max_length=MAX_NAME_LENGTH)
    description = models.CharField(max_length=MAX_DESCRIPTION_LENGTH)
    address = models.CharField(max_length=MAX_ADDRESS_LENGTH, default='')
    open_time = models.TimeField()
    close_time = models.TimeField()
    contact_email = models.EmailField(unique=True, default='example@example.com')
    contact_phone_number = PhoneNumberField(default='')
    venue_category = models.CharField(max_length=2, 
            choices=VENUE_CATEGORY_CHOICES,
            blank=True)
    hosting_events = models.ManyToManyField("EventModel", related_name="hosts", null=True)
    # image = models.URLField(max_length=MAX_URL_LENGTH)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)

    REQUIRED_FIELDS = ['lat', 'long', 'venue_category']

    def __str__(self):
        return self.name
