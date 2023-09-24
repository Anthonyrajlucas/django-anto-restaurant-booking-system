from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer_name', 'customer_email','date', 'start_time', 'end_time', ]

        date = forms.DateField(help_text="Date must be a future date")
        widgets = {"date": forms.widgets.DateInput(attrs={"type": "date"}),
                   'start_time': forms.TimeInput(attrs={'type': 'time'}),
                   'end_time': forms.TimeInput(attrs={'type': 'time'})}
        labels = {
            "customer_name": "Customer Name",
            "customer_email": "Customer Email",
            "date": "Booking Date",
            "start_time": "Start Time",
            "end_time": "End Time",
        }