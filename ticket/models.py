from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# Create your models here.


# guest -- movie -- reservation

class Movie(models.Model):
    hall = models.CharField(max_length=10)
    movie = models.CharField(max_length=50)
    date = models.DateField()

class Guest(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE , related_name='reservation')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE , related_name='reservation')


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)