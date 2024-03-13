from django.db import models

class WishlistModel(models.Model):
    user = models.ForeignKey("UserModel", on_delete=models.CASCADE)
    events = models.ManyToManyField("EventModel", related_name='wishlists', null=True)
    venues = models.ManyToManyField("VenueModel", related_name='wishlists', null=True)

    def __str__(self):
        return self.name