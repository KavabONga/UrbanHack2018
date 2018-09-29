from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


# Create your models here.

class Driver(models.Model):
    USERNAME_FIELD = 'login'

    login = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    route_info = models.TextField(default='')  # <время начала> <point1 coords> <point2 coords> ... <pointN coords>

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.login

class Passenger(models.Model):
    USERNAME_FIELD = 'login'

    login = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    route_info = models.TextField(default='')  # <время начала> <point1 coords> <point2 coords> ... <pointN coords>

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.login
