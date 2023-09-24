from django.contrib import admin
from .models import Booking

# Register your models here.
@admin.register(Booking)
class Booking(admin.ModelAdmin):
    list_display = (
        "customer_name",
        "customer_email",
        "date",
        "start_time",
        "end_time",
        "total_tables",
    )
