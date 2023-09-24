from django import forms
from .models import Booking
from django.core.exceptions import ValidationError
from django.utils import timezone


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer_name', 'customer_email', 'date', 'start_time', 'end_time', 'total_tables']

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        if date and date < timezone.now().date():
            raise ValidationError("Booking date cannot be in the past")

        if not self.instance.is_table_available():
            raise ValidationError("No tables available for this date")

    date = forms.DateField(
        help_text="Date must be a future date",
        widget=forms.widgets.DateInput(attrs={"type": "date"})
    )
    start_time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'})
    )
    end_time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'})
    )

    labels = {
        "customer_name": "Customer Name",
        "customer_email": "Customer Email",
        "date": "Booking Date",
        "start_time": "Start Time",
        "end_time": "End Time",
        "total_tables": "Total table size"
    }
