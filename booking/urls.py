from django.urls import path
from .views import BookingListView, BookingCreateView

urlpatterns = [
    path('bookings/', BookingListView.as_view(), name='booking_list'),
    path('bookings/new/', BookingCreateView.as_view(), name='booking-create'),
]
