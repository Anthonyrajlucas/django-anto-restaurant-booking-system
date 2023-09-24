from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Booking
from .forms import BookingForm
from django.contrib import messages 
from django.core.mail import send_mail  
from django.core.exceptions import ValidationError  
from django.db.models import Sum
from django.utils import timezone


class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'booking_list.html'
    context_object_name = 'bookings'
    ordering = ['-created_on']


class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    template_name = 'booking_form.html'
    form_class = BookingForm
    success_url = reverse_lazy('booking-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user

        # Check availability for the selected date
        selected_date = form.cleaned_data['date']
        
        # Calculate the total tables from all bookings on the same day
        total_tables_on_date = Booking.objects.filter(date=selected_date).aggregate(Sum('total_tables'))['total_tables__sum'] or 0

        if total_tables_on_date + form.instance.total_tables <= 25:
            form.save()
            messages.success(self.request, 'Booking successful!')
            subject = 'New Booking'
            message = 'A new booking has been made.'
            from_email = 'anthonyraj.lucas@gmail.com'
            recipient_list = ['anthonyraj.lucas@gmail.com']
            send_mail(subject, message, from_email, recipient_list, fail_silently=True)
        else:
            messages.error(self.request, 'No tables available for this date')
   
        return super().form_valid(form)


class BookingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Booking
    template_name = 'booking_form.html'
    form_class = BookingForm
    success_url = reverse_lazy('booking-list')

    def test_func(self):
        return self.request.user == self.get_object().created_by

    def form_valid(self, form):
        messages.success(self.request, 'Booking updated successfully!')
        return super().form_valid(form)


class BookingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Booking
    template_name = 'booking_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Booking deleted successfully')
        return super().delete(request, *args, **kwargs)

    success_url = reverse_lazy('booking-list')  

    def test_func(self):
        return self.request.user == self.get_object().created_by
