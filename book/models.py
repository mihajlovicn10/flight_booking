from django.db import models
from authentication import models as models_auth



# Create your models here.


class Flight(models.Model):
    from_city = models.CharField(max_length=30)
    to_city = models.CharField(max_length=30)
    departing = models.DateTimeField()
    airline_company = models.CharField(max_length=30)
    price = models.FloatField()
    def __str__(self):
        return f"{self.airline_company} {self.from_city} {self.to_city} {self.price}€"

class Booking(models.Model):
    user = models.ForeignKey(to=models_auth.User, on_delete=models.CASCADE)
    flight = models.ForeignKey(to=Flight, on_delete=models.CASCADE)
    datetime_of_booking = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user} {self.flight.from_city} {self.flight.to_city}"

    

