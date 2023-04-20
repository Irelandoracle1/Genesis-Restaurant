from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=True, blank=True)
    first_name = models.CharField(max_length=270)
    last_name = models.CharField(max_length=270)
    email = models.EmailField(null=False, blank=False)
    phone = models.CharField(max_length=11, null=True)
    date = models.DateField(default=datetime.now)
    time = models.TimeField()
    guests_number = models.IntegerField()
    special_message = models.CharField(max_length=450, null=True, blank=True)

    def __str__(self):
        return f'Name: {self.first_name} {self.last_name}'
