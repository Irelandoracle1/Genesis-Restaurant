from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('make-booking',
         views.BookingCreation.as_view(),
         name='booking_create'),
    path('booking-list/',
         views.BookingList.as_view(),
         name='booking_detail'),
    ]
