from rest_framework import routers
from django.conf.urls import include
from django.urls import path
# Following two lines added for media
from django.conf import settings
from django.conf.urls.static import static

from nashvillehotindexapi.views import register_user, login_user
from nashvillehotindexapi.views import Restaurants
from nashvillehotindexapi.views import RestaurantHeats
from nashvillehotindexapi.views import Orders, Profile


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'restaurants', Restaurants, 'restaurant')
router.register(r'restaurantheats', RestaurantHeats, 'restaurantheat')
router.register(r'orders', Orders, 'order')
router.register(r'profile', Profile, 'profile')

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]

#Added from youtube tutorial media test
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)