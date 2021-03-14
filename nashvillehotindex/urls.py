from nashvillehotindexapi.models.restaurant import Restaurant
from rest_framework import routers
from django.conf.urls import include
from django.urls import path
from nashvillehotindexapi.views import register_user, login_user
from nashvillehotindexapi.views import Restaurants
from nashvillehotindexapi.views import RestaurantHeats
from nashvillehotindexapi.views import Orders

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'restaurants', Restaurants, 'restaurant')
router.register(r'restaurantheats', RestaurantHeats, 'restaurantheat')
router.register(r'orders', Orders, 'order')

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
