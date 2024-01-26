from django.contrib.auth.models import User
from django.db import models

class EventPage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default = 1)
    heading = models.CharField(max_length=20)
    description = models.CharField(max_length=250)
    location = models.CharField(max_length = 25)
    event_time = models.TimeField()
    pass_out_year = models.DateField()
    event_date = models.DateField()
class RaiseHand(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default = 1)
    raisehand = models.BooleanField()

class RequestInstitute(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default = 1)
    request_institute_name = models.CharField(max_length=20)

class InstituteDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default = 1)
    department = models.CharField(max_length=20)
    graduation_year = models.DateField()

class EditProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default = 1)
    image_url = models.CharField(max_length=20)
    about_us = models.CharField(max_length=200)
