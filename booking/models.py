from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    total_tables = models.PositiveIntegerField(default=25)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def is_table_available(self):
        booked_tables = Booking.objects.filter(date=self.date).aggregate(Sum('total_tables'))['total_tables__sum'] or 0
        return booked_tables < 25

    def save(self, *args, **kwargs):
        if not self.booking_id: 
            if not self.is_table_available():
                raise Exception("No tables available for this date")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking ID: {self.booking_id}, Date: {self.date}"
