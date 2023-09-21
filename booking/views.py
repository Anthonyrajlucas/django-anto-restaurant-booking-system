from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Booking
from .forms import BookingForm



class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'booking/booking_list.html'
    context_object_name = 'bookings'
    ordering = ['-created_on']

class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    template_name = 'booking/booking_form.html'
    form_class = BookingForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class BookingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Booking
    template_name = 'booking/booking_form.html'
    form_class = BookingForm

    def test_func(self):
        return self.request.user == self.get_object().created_by

class BookingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Booking
    template_name = 'booking/booking_confirm_delete.html'
    success_url = reverse_lazy('booking-list')

    def test_func(self):
        return self.request.user == self.get_object().created_by
