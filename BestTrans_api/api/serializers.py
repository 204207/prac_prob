from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import (
    Profile, Order, Offer, Driver, Vehicle, BestTransData, SimpleAddress, ExtendAddress, Cargo)
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        #read_only_fields = ('id',)
        extra_kwargs = {'password': {'required': True, 'write_only': True}}


class SimpleAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleAddress
        fields = '__all__'


class ExtendAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendAddress
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    address = SimpleAddressSerializer(many=False)

    class Meta:
        model = Profile
        fields = '__all__'
        #depth = 2
        #exclude = ('address',)

    # def create(self, validated_data):
    #     user = User.objects.create_user(validated_data["user"])
    #     profile = Profile.objects.create(user=user, name=validated_data["name"], surname=validated_data["surname"],
    #                                      email=validated_data['email'], phone_number=validated_data["phone_number"],
    #                                      company=validated_data["company"], tax_number=validated_data["tax_number"],
    #                                      address=validated_data["address"])
    #     return profile


class BestTransDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestTransData
        fields = '__all__'


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    performer = BestTransDataSerializer(many=False)
    loading_place = ExtendAddressSerializer()
    destination = ExtendAddressSerializer()
    cargo = CargoSerializer()

    class Meta:
        model = Order
        fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):
    loading_place = ExtendAddressSerializer()
    destination = ExtendAddressSerializer()

    class Meta:
        model = Offer
        fields = '__all__'
        depth = 2


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'
