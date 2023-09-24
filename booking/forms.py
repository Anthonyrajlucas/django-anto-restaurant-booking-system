from django import forms
from .models import Booking
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer_name', 'customer_email', 'date', 'start_time', 'end_time', 'total_tables']

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        if date and date < timezone.now().date():
            raise ValidationError("Date must be a future date")

        if not self.instance.is_table_available():
            raise ValidationError("No tables available for this date")

        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")

        # Define the allowed time range from 10:00 AM to 10:00 PM
        allowed_start_time = datetime.strptime("10:00 AM", "%I:%M %p").time()
        allowed_end_time = datetime.strptime("10:00 PM", "%I:%M %p").time()

        if start_time and end_time and (start_time < allowed_start_time or end_time > allowed_end_time):
            raise ValidationError("Start and End time should be between 10:00 AM and 10:00 PM")
        
        total_tables = cleaned_data.get("total_tables")
        if total_tables and total_tables > 25:
            raise ValidationError("Total tables cannot exceed 25")

    date = forms.DateField(
        help_text="Date must be a future date",
        widget=forms.widgets.DateInput(attrs={"type": "date"}),
    )
    start_time = forms.TimeField(
        help_text="Start time should be after 10:00 AM",
        widget=forms.TimeInput(attrs={'type': 'time'}),
    )
    end_time = forms.TimeField(
        help_text="End time should be before 10:00 PM",
        widget=forms.TimeInput(attrs={'type': 'time'}),
    )

    labels = {
        "customer_name": "Customer Name",
        "customer_email": "Customer Email",
        "date": "Date",
        "start_time": "Start Time",
        "end_time": "End Time",
        "total_tables": "Total table size"
    }
