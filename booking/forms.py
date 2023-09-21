from django import forms
from .models import Booking



class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'start_time', 'end_time', 'customer_name', 'customer_email']
