from django.db import models
# from django.contrib.auth.models import User

class WishlistModel(models.Model):
    # user = models.ForeignKey("UserModel", on_delete=models.CASCADE)
    events = models.ManyToManyField("EventModel", related_name='wishlists')
    venues = models.ManyToManyField("VenueModel", related_name='wishlists')

    def __str__(self):
        return f'Wishlist of {self.user.username}'