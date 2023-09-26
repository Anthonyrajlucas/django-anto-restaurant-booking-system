from django import forms
from .models import Booking
from django.utils import timezone
from datetime import datetime
from django.db.models import Sum


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer_name', 'customer_email', 'date', 'booking_time', 'total_tables']

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        if date and date < timezone.now().date():
            raise forms.ValidationError("Date must be a future date")

        booking_time = cleaned_data.get("booking_time")
        if date == timezone.now().date() and booking_time:
            current_time = datetime.now().time().strftime("%H:%M")
            if booking_time < current_time:
                raise forms.ValidationError("Booking time cannot be in the past for today's date")

        total_tables = cleaned_data.get("total_tables")
        if total_tables and total_tables > 25:
            raise forms.ValidationError("Total tables cannot exceed 25")

        # Check if the total_tables for the selected date and time exceed 25
        if date and booking_time:
            total_tables_on_datetime = Booking.objects.filter(date=date, booking_time=booking_time).exclude(pk=self.instance.pk).aggregate(Sum('total_tables'))['total_tables__sum'] or 0
            if total_tables_on_datetime + total_tables > 25:
                raise forms.ValidationError("No tables available for this date and time")

    date = forms.DateField(
        help_text="Date must be a future date",
        widget=forms.widgets.DateInput(attrs={"type": "date"}),
    )
    booking_time = forms.ChoiceField(
        choices=[("10:00", "10:00 AM"), ("11:00", "11:00 AM"), ("12:00", "12:00 PM"),
                 ("13:00", "01:00 PM"), ("14:00", "02:00 PM"), ("15:00", "03:00 PM"),
                 ("16:00", "04:00 PM"), ("17:00", "05:00 PM"), ("18:00", "06:00 PM"),
                 ("19:00", "07:00 PM"), ("20:00", "08:00 PM"), ("21:00", "09:00 PM"),
                 ("22:00", "10:00 PM")],
        help_text="Select a booking time between 10:00 AM and 10:00 PM"
    )

    labels = {
        "customer_name": "Customer Name",
        "customer_email": "Customer Email",
        "date": "Date",
        "booking_time": "Booking Time",
        "total_tables": "Total table size"
    }
