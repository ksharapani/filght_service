from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Flight(models.Model):
    max_weight = models.IntegerField()
    max_capacity = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Booking(models.Model):
    objects = None

    date = models.DateField()
    start_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='start_location')
    end_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='end_location')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    weight = models.IntegerField()
    capacity = models.IntegerField()
    status = models.BooleanField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
