from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=128)
    middle_name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    date_of_birth = models.DateField()
    country_code = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=32)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


