from django.shortcuts import render
from .models import Booking
from django.views import generic

# Create your views here.


class HomePage(generic.ListView):
    model = Booking
    template_name = 'booking/index.html'
