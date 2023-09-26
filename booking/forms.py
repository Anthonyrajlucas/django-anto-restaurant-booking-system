from django import forms
from .models import Booking
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer_name', 'customer_email', 'date', 'booking_time', 'total_tables']

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        if date and date < timezone.now().date():
            raise ValidationError("Date must be a future date")

        booking_time = cleaned_data.get("booking_time")
        if date == timezone.now().date() and booking_time:
            current_time = datetime.now().time().strftime("%H:%M")
            if booking_time < current_time:
                raise ValidationError("Booking time cannot be in the past for today's date")

        if not self.instance.is_table_available():
            raise ValidationError("No tables available for this date and time")

        total_tables = cleaned_data.get("total_tables")
        if total_tables and total_tables > 25:
            raise ValidationError("Total tables cannot exceed 25")

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
    )

    labels = {
        "customer_name": "Customer Name",
        "customer_email": "Customer Email",
        "date": "Date",
        "booking_time": "Booking Time",
        "total_tables": "Total table size"
    }
