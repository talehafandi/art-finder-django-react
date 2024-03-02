from django.db import models
# Create your models here.

# EVENT MODEL
class EventModel(models.Model):
    MAX_TITLE_LENGTH = 32
    MAX_DESCRIPTION_LENGTH = 200
    MAX_URL_LENGTH = 200

    # Enum for the event types
    ART = "AR"
    PHOTOGRAPHY = "PH"
    SCULPTURE = "SU"
    CRAFTS = "CR"

    EVENT_CATEGORY_CHOICES = [
        (ART, "ART"),
        (PHOTOGRAPHY, "PHOTOGRAPHY"),
        (SCULPTURE, "SCULPTURE"),
        (CRAFTS, "CRAFTS"),
    ]

    # Event model fields
    title = models.CharField(max_length=MAX_TITLE_LENGTH)
    description = models.CharField(max_length=MAX_DESCRIPTION_LENGTH)
    venue = models.OneToOneField("VenueModel", on_delete=models.CASCADE, related_name="hosted_in")
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    event_category = models.CharField(max_length=2, 
            choices=EVENT_CATEGORY_CHOICES,
            default=ART)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    # image = models.URLField(max_length=MAX_URL_LENGTH)

    def __str__(self):
        return self.name