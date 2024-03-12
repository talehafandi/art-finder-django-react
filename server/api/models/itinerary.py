from django.db import models

# ITINERARY MODEL
class ItineraryModel(models.Model):
    MAX_NAME_LENGTH = 16
    MAX_DESCRIPTION_LENGTH = 200

    name = models.CharField(max_length=64)
    description = models.CharField(max_length=MAX_DESCRIPTION_LENGTH)
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey("UserModel", on_delete=models.CASCADE, related_name='itineraries')
    venues = models.ManyToManyField("VenueModel", related_name='itineraries', null=True)

    def __str__(self):
        return self.name