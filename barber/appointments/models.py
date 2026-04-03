from django.db import models
from django.contrib.auth.models import User
from services.models import Service

# Create your models here.
    
class Barber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    status = models.CharField(max_length=20, default='scheduled')

    def __str__(self):
        return f"{self.user.username} - {self.service.name} at {self.date_time}"