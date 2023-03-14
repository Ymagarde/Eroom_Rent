from email.headerregistry import Address
from django.db import models

class Ownerreg(models.Model):
    emailid = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    address = models.CharField(max_length=50)


class Brokerreg(models.Model):
    emailid = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

class Customerreg(models.Model):
    emailid = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

class Customer(models.Model):
    name = models.CharField(max_length=50)
    emailid = models.CharField(max_length=50)
    bookid = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    Category = models.CharField(max_length=100,default="")

class Property(models.Model):
    Category = models.CharField(max_length=100)
    Rent = models.CharField(max_length=100)
    Location = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
