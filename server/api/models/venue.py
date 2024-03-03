from django.db import models

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
    # address = models.CharField(max_length=MAX_ADDRESS_LENGTH)
    openTime = models.TimeField()
    closeTime = models.TimeField()
    contactEmail = models.EmailField()
    # contactPhoneNumber= models.IntegerField()
    venueCategory = models.CharField(max_length=2, 
            choices=VENUE_CATEGORY_CHOICES,
            blank=True, null=True)
    # image = models.URLField(max_length=MAX_URL_LENGTH)
    hostingEvents = models.ForeignKey("EventModel", on_delete=models.CASCADE, related_name="hosts")

    def __str__(self):
        return self.name
