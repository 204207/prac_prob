"""BestTrans_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api import views
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
router.register(r'profiles', views.ProfileViewSet)
router.register(r'offers', views.OfferViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'drivers', views.DriverViewSet)
router.register(r'vehicles', views.VehicleViewSet)
# router.register(r'cargos', views.VehicleViewSet)
# router.register(r'simple-addresses', views.VehicleViewSet)
# router.register(r'extend-addresses', views.VehicleViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', obtain_auth_token)
]

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.