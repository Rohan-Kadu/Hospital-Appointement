from django.db import models

# Create your models here.
class userRequest(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Address = models.TextField(max_length=50)
    Gender = models.CharField(max_length=50)
    Contact = models.BigIntegerField()
    Date = models.DateField()
    Time = models.TextField(max_length=30)
    SelectDoctor = models.CharField(max_length=50)
    Comment = models.CharField(max_length=50)


class adminDb(models.Model):
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)





class approvedReq(models.Model):
    AppointementId = models.BigIntegerField()
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Address = models.TextField(max_length=50)
    Gender = models.CharField(max_length=50)
    Contact = models.BigIntegerField()
    Date = models.DateField()
    Time = models.TextField(max_length=30)
    SelectDoctor = models.CharField(max_length=50)
    Comment = models.CharField(max_length=50)    