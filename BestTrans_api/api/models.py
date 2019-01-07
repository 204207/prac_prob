from django.db import models
from django.contrib.auth.models import User


class SimpleAddress(models.Model):
    street = models.CharField(max_length=64)
    post_code = models.CharField(max_length=64)
    place = models.CharField(max_length=64)
    country = models.CharField(max_length=64)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=32)
    company = models.CharField(max_length=64, blank=True)
    tax_number = models.CharField(max_length=32)
    address = models.ForeignKey(SimpleAddress, on_delete=models.SET_NULL, null=True, blank=True)


class BestTransData(models.Model):
    name = models.CharField(default="BestTrans Sp z o.o", max_length=64)
    tax_number = models.CharField(default="123 456 78 90", max_length=64)
    street = models.CharField(default="ul. Piotrkowska 102", max_length=64)
    post_code = models.CharField(default="90-010 Łódź", max_length=64)
    place = models.CharField(default="Łódź", max_length=64)
    country = models.CharField(default="Poland", max_length=64)


class Driver(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=32)
    card_drive_number = models.CharField(max_length=32)


class Vehicle(models.Model):
    brand = models.CharField(max_length=32)
    type = models.CharField(max_length=32)
    registration_number = models.CharField(max_length=32)


class ExtendAddress(models.Model):
    date = models.DateTimeField()
    hour = models.TimeField()
    name = models.CharField(max_length=32, default="")
    place = models.ForeignKey(SimpleAddress, on_delete=models.SET_NULL, null=True, blank=True)
    remarks = models.TextField(max_length=256, default="")


class Offer(models.Model):
    loading_place = models.OneToOneField(ExtendAddress, related_name='%(class)s_loading_place_offer', on_delete=models.CASCADE)
    destination = models.OneToOneField(ExtendAddress, related_name='%(class)s_destination_place_offer', on_delete=models.CASCADE)
    vehicle = models.ManyToManyField(Vehicle, null=True, blank=True)
    pallets_number = models.IntegerField()
    additional_remarks = models.TextField(max_length=256, default="")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField(default=True)


class Cargo(models.Model):
    wrapping = models.CharField(max_length=64, default="")
    pallets_number = models.IntegerField()
    additional_remarks = models.TextField(max_length=256, default="")


class Order(models.Model):
    customer = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    performer = models.ForeignKey(BestTransData, null=True, on_delete=models.SET_NULL)
    offer = models.ForeignKey(Offer, null=True,  on_delete=models.SET_NULL, blank=True)
    driver = models.ManyToManyField(Driver, null=True, blank=True)
    vehicle = models.ManyToManyField(Vehicle, null=True, blank=True)
    loading_place = models.OneToOneField(ExtendAddress, related_name='%(class)s_loading_place_order', on_delete=models.CASCADE)
    destination = models.OneToOneField(ExtendAddress, related_name='%(class)s_destination_place_order', on_delete=models.CASCADE)
    additional_remarks = models.TextField(max_length=256, default="")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()
    is_active = models.BooleanField(default=True)
    cargo = models.OneToOneField(Cargo, on_delete=models.CASCADE, null=True, blank=True)
