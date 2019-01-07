from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import (
    Profile, Order, Offer, Driver, Vehicle, BestTransData, SimpleAddress, ExtendAddress, Cargo)
from .serializers import (
    ProfileSerializer, OrderSerializer, OfferSerializer, DriverSerializer, VehicleSerializer, BestTransDataSerializer,
    SimpleAddressSerializer, ExtendAddressSerializer, CargoSerializer)
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from django.http.response import HttpResponseNotAllowed
import datetime
from rest_framework.authtoken.models import Token


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = (TokenAuthentication,)

    def create(self, request, *args, **kwargs):
        user = request.data['user']
        user = User.objects.create_user(username=user['username'], password=user['password'])
        address = request.data["address"]
        Token.objects.create(user=user)
        profile = Profile.objects.create(user=user, name=request.data["name"], surname=request.data["surname"],
                                         email=request.data['email'], phone_number=request.data["phone_number"],
                                         company=request.data["company"], tax_number=request.data["tax_number"],
                                         address=SimpleAddress.objects.create(street=address['street'],
                                                                              post_code=address['post_code'],
                                                                              place=address['place'], country=address['country']))

        serializer = self.get_serializer(profile, many=False)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        if request.user.is_active:
            instance = self.get_object()
            serializer = self.get_serializer(instance, many=False)
            return Response(serializer.data)
        else:
            return HttpResponseNotAllowed('Not allowed')

    def update(self, request, *args, **kwargs):
        if request.user.is_active:
            profile = self.get_object()
            profile.name = request.data['name']
            profile.surname = request.data['surname']
            profile.phone_number = request.data['phone_number']
            profile.company = request.data['company']
            profile.tax_number = request.data['tax_number']
            address = request.data["address"]
            profile.address = SimpleAddress.objects.create(street=address['street'], post_code=address['post_code'],
                                                           place=address['place'], country=address['country'])
            profile.email = request.data['email']
            #profile.user.password = request.data['password']
            profile.save()

            serializer = ProfileSerializer(profile, many=False)
            return Response(serializer.data)
        else:
            return HttpResponseNotAllowed('Not allowed')

    def list(self, request, *args, **kwargs):
        if request.user.is_superuser:
            all_profiles = Profile.objects.all()
            serializer = ProfileSerializer(all_profiles, many=True)
            return Response(serializer.data)
        else:
            return HttpResponseNotAllowed('Not allowed')

    def destroy(self, request, *args, **kwargs):
        if request.user.is_superuser:
            profil = self.get_object()
            profil.delete()
            return Response('Profile deleted')
        else:
            return HttpResponseNotAllowed('Not allowed')

    @action(detail=True, methods=['get'])
    def get_active_orders(self, request, *args, **kwargs):
        if request.user.is_active:
            profile = self.get_object()
            active_orders = profile.order_set.filter(is_active=True)
            serializer = ProfileSerializer(active_orders, context={'request': request}, many=True)
            return Response(serializer.data)
        else:
            return HttpResponseNotAllowed('Not allowed')

    @action(detail=True, methods=['get'])
    def get_past_orders(self, request, *args, **kwargs):
        if request.user.is_active:
            profile = self.get_object()
            past_orders = profile.order_set.filter(is_active=False)
            serializer = ProfileSerializer(past_orders, context={'request': request}, many=True)
            return Response(serializer.data)
        else:
            return HttpResponseNotAllowed('Not allowed')

    @action(detail=True, methods=['get'])
    def get_orders(self, request, *args, **kwargs):
        if request.user.is_active:
            profile = self.get_object()
            orders = profile.order_set.all()
            serializer = ProfileSerializer(orders, context={'request': request}, many=True)
            return Response(serializer.data)
        else:
            return HttpResponseNotAllowed('Not allowed')

    @action(detail=True, methods=['post'])
    def add_order(self, request, *args, **kwargs):
        if request.user.is_active:
            profile = self.get_object()
            order = Order.objects.get(id=request.data['order'])
            order.customer.add(profile)

            serializer = ProfileSerializer(profile, context={'request': request}, many=False)
            return Response(serializer.data)
        else:
            return HttpResponseNotAllowed('Not allowed')


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = (TokenAuthentication,)

    @action(detail=False, methods=['get'])
    def get_active_orders(self, request, *args, **kwargs):
        if request.user.is_superuser:
            active_orders = Order.objects.filter(is_active=True)
            serializer = OrderSerializer(active_orders, many=True)
            return Response(serializer.data)
        else:
            return HttpResponseNotAllowed('Not allowed')

    @action(detail=False, methods=['get'])
    def get_past_orders(self, request, *args, **kwargs):
        if request.user.is_superuser:
            past_orders = Order.objects.filter(is_active=False)
            serializer = OrderSerializer(past_orders, many=True)
            return Response(serializer.data)
        else:
            return HttpResponseNotAllowed('Not allowed')

    def list(self, request, *args, **kwargs):
        if request.user.is_superuser:
            all_orders = Order.objects.all()
            serializer = OrderSerializer(all_orders, many=True)
            return Response(serializer.data)
        else:
            return HttpResponseNotAllowed('Not allowed')

    def retrieve(self, request, *args, **kwargs):
        if request.user.is_active:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            return HttpResponseNotAllowed('Not allowed')

    def create(self, request, *args, **kwargs):
        if request.user.is_superuser:
            customer = Profile.objects.get(id=request.data['customer'])
            performer = request.data['performer']
            performer = BestTransData.objects.get(id=performer['id'])
            offer = Offer.objects.get(id=request.data['offer'])
            loading_place = request.data['loading_place']
            simple_start_place = SimpleAddress.objects.get(id=loading_place['place'])
            loading_place = ExtendAddress.objects.create(date=loading_place['date'], hour=loading_place['hour'],
                                                         name=loading_place['name'], remarks=loading_place['remarks'],
                                                         place=simple_start_place)
            destination = request.data['destination']
            simple_stop_place = SimpleAddress.objects.get(id=destination['place'])
            destination = ExtendAddress.objects.create(date=destination['date'], hour=destination['hour'],
                                                       name=destination['name'], remarks=destination['remarks'],
                                                       place=simple_stop_place)
            cargo = request.data['cargo']
            cargo = Cargo.objects.create(wrapping=cargo['wrapping'], pallets_number=cargo['pallets_number'],
                                         additional_remarks=cargo['additional_remarks'])

            order = Order.objects.create(customer=customer, performer=performer, offer=offer,
                                         loading_place=loading_place, destination=destination,
                                         additional_remarks=request.data['additional_remarks'], price=request.data['price'],
                                         date=request.data['date'], is_active=request.data['is_active'], cargo=cargo
                                         )

            driver = Driver.objects.get(id=request.data['driver'])
            order.driver.add(driver)
            vehicle = Vehicle.objects.get(id=request.data['vehicle'])
            order.vehicle.add(vehicle)

            serializer = OrderSerializer(order, many=False)
            return Response(serializer.data)
        else:
            return HttpResponseNotAllowed('Not allowed')

    def destroy(self, request, *args, **kwargs):
        if request.user.is_superuser:
            order = self.get_object()
            order.delete()
            return Response('Order deleted')
        else:
            return HttpResponseNotAllowed('Not allowed')

    def update(self, request, *args, **kwargs):
        if request.user.is_superuser: #and datetime.datetime.now() < self.get_object().loading_place.date:
            order = self.get_object()
            order.customer = Profile.objects.get(id=request.data['customer'])
            performer = request.data['performer']
            order.performer = BestTransData.objects.get(id=performer['id'])
            order.offer = Offer.objects.get(id=request.data['offer'])
            start_place = request.data['loading_place']
            place = SimpleAddress.objects.get(id=start_place['place'])
            loading_place = ExtendAddress.objects.create(date=start_place['date'], hour=start_place['hour'],
                                                         name=start_place['name'],place=place,
                                                         remarks=start_place['remarks'])
            order.loading_place = loading_place

            stop_place = request.data['destination']
            place = SimpleAddress.objects.get(id=start_place['place'])
            destination = ExtendAddress.objects.create(date=stop_place['date'], hour=stop_place['hour'],
                                                       name=stop_place['name'], place=place,
                                                       remarks=stop_place['remarks'])
            order.destination = destination

            vehicle = Vehicle.objects.get(id=request.data['vehicle'])
            order.vehicle.add(vehicle)
            driver = Driver.objects.get(id=request.data['driver'])
            order.driver.add(driver)
            order.additional_remarks = request.data['additional_remarks']
            order.price = request.data['price']
            order.date = request.data['date']
            order.is_active = request.data['is_active']
            cargo = request.data['cargo']
            order.cargo = Cargo.objects.create(wrapping=cargo['wrapping'], pallets_number=cargo['pallets_number'],
                                               additional_remarks=cargo['additional_remarks'])

            order.save()
            serializer = OrderSerializer(order, many=False)
            return Response(serializer.data)
        else:
            return HttpResponseNotAllowed('Not allowed')

    @action(detail=False, methods=['get'])
    def close(self, request, *args, **kwargs):
        if request.user.is_superuser:
            ids = request.data['ids']
            orders = []
            for one_id in ids:
                order = Offer.objects.get(id=one_id)
                order.is_active = False
                order.save()
                orders.append(order)

            serializer = OfferSerializer(orders, many=True)
            return Response(serializer.data)
        else:
            return HttpResponseNotAllowed('Not allowed')

    @action(detail=False, methods=['get'])
    def open(self, request, *args, **kwargs):
        if request.user.is_superuser:
            ids = request.data['ids']
            orders = []
            for one_id in ids:
                order = Offer.objects.get(id=one_id)
                order.is_active = True
                order.save()
                orders.append(order)

            serializer = OfferSerializer(orders, many=True)
            return Response(serializer.data)
        else:
            return HttpResponseNotAllowed('Not allowed')


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    authentication_classes = (TokenAuthentication,)

    def list(self, request, *args, **kwargs):
        offers = Offer.objects.filter(is_active=True)
        serializer = OfferSerializer(offers, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['put'])
    def close(self, request, *args, **kwargs):
        if request.user.is_superuser:
            ids = request.data['ids']
            offers = []
            for one_id in ids:
                offer = Offer.objects.get(id=one_id)
                offer.is_active = False
                offer.save()
                offers.append(offer)

            serializer = OfferSerializer(offers, many=True)
            return Response(serializer.data)
        else:
            return HttpResponseNotAllowed('Not allowed')

    @action(detail=False, methods=['put'])
    def open(self, request, *args, **kwargs):
        if request.user.is_superuser:
            ids = request.data['ids']
            offers = []
            for one_id in ids:
                offer = Offer.objects.get(id=one_id)
                offer.is_active = True
                offer.save()
                offers.append(offer)

            serializer = OfferSerializer(offers, many=True)
            return Response(serializer.data)
        else:
            return HttpResponseNotAllowed('Not allowed')

    def create(self, request, *args, **kwargs):
        if request.user.is_superuser:
            start_place = request.data['loading_place']
            start_simple_address = start_place['place']
            load_place = SimpleAddress.objects.create(street=start_simple_address['street'], post_code=start_simple_address['post_code'],
                                                      place=start_simple_address['place'], country=start_simple_address['country'])
            loading_place = ExtendAddress.objects.create(date=start_place['date'], hour=start_place['hour'], name=start_place['name'],
                                                         place=load_place, remarks=start_place['remarks'])

            stop_place = request.data['destination']
            stop_simple_address = stop_place['place']
            destination_place = SimpleAddress.objects.create(street=stop_simple_address['street'],
                                                             post_code=stop_simple_address['post_code'],
                                                             place=stop_simple_address['place'],
                                                             country=stop_simple_address['country'])
            destination = ExtendAddress.objects.create(date=stop_place['date'], hour=stop_place['hour'],
                                                       name=stop_place['name'], place=destination_place,
                                                       remarks=stop_place['remarks'])

            vehicle = Vehicle.objects.get(id=request.data['vehicle'])
            offer = Offer.objects.create(loading_place=loading_place, destination=destination,
                                         pallets_number=request.data['pallets_number'],
                                         additional_remarks=request.data['additional_remarks'], price=request.data['price'],
                                         is_active=request.data['is_active'])

            offer.vehicle.add(vehicle)
            serializer = OfferSerializer(offer, many=False)
            return Response(serializer.data)
        else:
            return HttpResponseNotAllowed('Not allowed')

    def destroy(self, request, *args, **kwargs):
        if request.user.is_superuser:
            offer = self.get_object()
            offer.delete()
            return Response('Offer deleted')
        else:
            return HttpResponseNotAllowed('Not allowed')

    def update(self, request, *args, **kwargs):
        if request.user.is_superuser:
            offer = self.get_object()
            start_place = request.data['loading_place']
            start_simple_address = start_place['place']
            load_place = SimpleAddress.objects.create(street=start_simple_address['street'],
                                                      post_code=start_simple_address['post_code'],
                                                      place=start_simple_address['place'],
                                                      country=start_simple_address['country'])
            loading_place = ExtendAddress.objects.create(date=start_place['date'], hour=start_place['hour'],
                                                         name=start_place['name'],
                                                         place=load_place, remarks=start_place['remarks'])
            offer.loading_place = loading_place

            stop_place = request.data['destination']
            stop_simple_address = stop_place['place']
            destination_place = SimpleAddress.objects.create(street=stop_simple_address['street'],
                                                             post_code=stop_simple_address['post_code'],
                                                             place=stop_simple_address['place'],
                                                             country=stop_simple_address['country'])
            destination = ExtendAddress.objects.create(date=stop_place['date'], hour=stop_place['hour'],
                                                       name=stop_place['name'],place=destination_place,
                                                       remarks=stop_place['remarks'])
            offer.destination = destination
            vehicle = Vehicle.objects.get(id=request.data['vehicle'])
            offer.vehicle.add(vehicle)
            offer.pallets_number = request.data['pallets_number']
            offer.additional_remarks = request.data['additional_remarks']
            offer.price = request.data['price']
            offer.is_active = request.data['is_active']
            offer.save()

            serializer = OfferSerializer(offer, many=False)
            return Response(serializer.data)
        else:
            return HttpResponseNotAllowed('Not allowed')


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    authentication_classes = (TokenAuthentication,)

    def list(self, request, *args, **kwargs):
        if request.user.is_superuser:
            all_drivers = Driver.objects.all()
            serializer = DriverSerializer(all_drivers, context={'request': request}, many=True)
            return Response(serializer.data)
        else:
            return HttpResponseNotAllowed('Not allowed')

    def retrieve(self, request, *args, **kwargs):
        if request.user.is_superuser:
            instance = self.get_object()
            serializer = self.get_serializer(instance, context={'request': request}, many=False)
            return Response(serializer.data)
        else:
            return HttpResponseNotAllowed('Not allowed')

    def create(self, request, *args, **kwargs):
        if request.user.is_superuser:
            driver = Driver.objects.create(name=request.data['name'], surname=request.data['surname'], phone_number=request.data['phone_number'],
                                           card_drive_number=request.data['card_drive_number'])
            serializer = DriverSerializer(driver, context={'request': request}, many=False)
            return Response(serializer.data)
        else:
            return HttpResponseNotAllowed('Not allowed')

    def update(self, request, *args, **kwargs):
        if request.user.is_superuser:
            driver = self.get_object()
            driver.name = request.data['name']
            driver.surname = request.data['surname']
            driver.phone_number = request.data['phone_number']
            driver.card_drive_number = request.data['card_drive_number']
            driver.save()

            serializer = DriverSerializer(driver, context={'request': request}, many=False)
            return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        if request.user.is_superuser:
            driver = self.get_object()
            driver.delete()
            return Response('Driver deleted')
        else:
            return HttpResponseNotAllowed('Not allowed')


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    authentication_classes = (TokenAuthentication,)

    def list(self, request, *args, **kwargs):
        if request.user.is_superuser:
            all_vehicles = Vehicle.objects.all()
            serializer = VehicleSerializer(all_vehicles, context={'request': request}, many=True)
            return Response(serializer.data)
        else:
            return HttpResponseNotAllowed('Not allowed')

    def retrieve(self, request, *args, **kwargs):
        if request.user.is_superuser:
            instance = self.get_object()
            serializer = self.get_serializer(instance, context={'request': request}, many=False)
            return Response(serializer.data)
        else:
            return HttpResponseNotAllowed('Not allowed')

    def create(self, request, *args, **kwargs):
        if request.user.is_superuser:
            vehicle = Vehicle.objects.create(brand=request.data['brand'], type=request.data['type'],
                                             registration_number=request.data['registration_number'])
            serializer = VehicleSerializer(vehicle, context={'request': request}, many=False)
            return Response(serializer.data)
        else:
            return HttpResponseNotAllowed('Not allowed')

    def update(self, request, *args, **kwargs):
        if request.user.is_superuser:
            vehicle = self.get_object()
            vehicle.brand = request.data['brand']
            vehicle.type = request.data['type']
            vehicle.registration_number = request.data['registration_number']
            vehicle.save()

            serializer = VehicleSerializer(vehicle, context={'request': request}, many=False)
            return Response(serializer.data)
        else:
            return HttpResponseNotAllowed('Not allowed')

    def destroy(self, request, *args, **kwargs):
        if request.user.is_superuser:
            vehicle = self.get_object()
            vehicle.delete()
            return Response('Vehicle deleted')
        else:
            return HttpResponseNotAllowed('Not allowed')


class BestTransDataViewSet(viewsets.ModelViewSet):
    queryset = BestTransData.objects.all()
    serializer_class = BestTransDataSerializer


class SimpleAddressViewSet(viewsets.ModelViewSet):
    queryset = SimpleAddress.objects.all()
    serializer_class = SimpleAddressSerializer


class ExtendAddressViewSet(viewsets.ModelViewSet):
    queryset = ExtendAddress.objects.all()
    serializer_class = ExtendAddressSerializer


class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
