from django.db import models
# from django.contrib.auth.models import User

class BookingModel(models.Model):
    # user = models.ForeignKey("UserModel", on_delete=models.CASCADE)
    event = models.ForeignKey("EventModel", on_delete=models.CASCADE)
    number_of_tickets = models.IntegerField()
    booking_date = models.DateField()

    # class Meta:
    #     unique_together = ('user', 'event')  # Ensure uniqueness of user-event pair

    def __str__(self):
        return f'{self.user.username} booked for {self.event}'

