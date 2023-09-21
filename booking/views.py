from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView
from .models import Booking


class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'booking/booking_list.html'
    context_object_name = 'bookings'
    ordering = ['-created_on']


class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    template_name = 'booking/booking_form.html'
    fields = ['date', 'start_time', 'end_time', 'customer_name', 'customer_email']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)    


