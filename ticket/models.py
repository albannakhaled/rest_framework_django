from django.db import models

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
    