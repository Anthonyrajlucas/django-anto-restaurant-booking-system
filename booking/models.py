from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Booking ID: {self.booking_id}, Date: {self.date}"
