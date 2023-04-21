from django.shortcuts import render
from .models import Booking
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.

# This is the HomePage View


class HomePage(generic.ListView):
    model = Booking
    template_name = 'booking/index.html'


# This is the Booking Creation Page


class BookingCreation(generic.CreateView):
    model = Booking
    template_name = 'booking/booking_page.html'
    fields = ['first_name', 'last_name', 'email', 'phone', 'date', 'time', 'guests_number', 'special_message']
    success_url = reverse_lazy('home')
