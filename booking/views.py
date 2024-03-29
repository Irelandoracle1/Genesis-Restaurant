from django.shortcuts import render
from .models import Booking
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.

# This is the HomePage View


class HomePage(generic.ListView):
    model = Booking
    template_name = 'booking/index.html'

# This is the MenuPage View


class MenuPage(generic.ListView):
    model = Booking
    template_name = 'booking/restaurant_menu.html'


# This is the Booking Creation Page


class BookingCreation(LoginRequiredMixin, generic.CreateView):
    model = Booking
    template_name = 'booking/booking_page.html'
    fields = ['first_name', 'last_name', 'email',
              'phone', 'date', 'time', 'guests_number',
              'special_message']
    success_url = reverse_lazy('booking_detail')

    def form_valid(self, form):
        booking = form.save(commit=False)
        booking.user = self.request.user
        booking.save()
        return super().form_valid(form)


class BookingList(LoginRequiredMixin, generic.ListView):
    model = Booking
    template_name = 'booking/booking_detail.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        logged_user = self.request.user
        return Booking.objects.filter(user=logged_user)


class BookingUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Booking
    template_name = 'booking/booking_update.html'
    fields = ['first_name', 'last_name', 'email',
              'phone', 'date', 'time',
              'guests_number', 'special_message']
    success_url = reverse_lazy('booking_detail')


class BookingDelete(LoginRequiredMixin, generic.DeleteView):
    model = Booking
    template_name = 'booking/booking_confirm_delete.html'
    success_url = reverse_lazy('booking_detail')
