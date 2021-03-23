from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from nashvillehotindexapi.models import RestaurantHeat
from nashvillehotindexapi.models import Restaurant
from nashvillehotindexapi.models import Rating
from nashvillehotindexapi.models import Order
from rest_framework.decorators import action

class RestaurantHeats(ViewSet):


    def retrieve(self, request, pk=None):
        """Handle GET requests for single game

        Returns:
            Response -- JSON serialized game instance
        """
        restaurant = Restaurant.objects.get(pk=pk)
        
        try:
            # `pk` is a parameter to this function, and
            # Django parses it from the URL route parameter
            #   http://localhost:8000/games/2
            #
            # The `2` at the end of the route becomes `pk`
            # restaurant_heat_levels = RestaurantHeat.objects.filter(restaurant=restaurant)
            restaurantheat = RestaurantHeat.objects.get(pk=pk)
            restaurantheat = RestaurantHeat.objects.filter(restaurant__id = restaurant.id)
            serializer = RestaurantHeatSerializer(restaurantheat, many=True, context={'request': request})
            return Response(serializer.data)
        except ValueError as ex:
            return HttpResponseServerError(ex, status=status.HTTP_404_NOT_FOUND) 
    
    def list(self, request):
        """Handle GET requests to games resource

        Returns:
            Response -- JSON serialized list of games
        """
        # Get all Restaurant Heats from the database. Only needed if stretch goal
        # met for listing hottest heats 
        restaurants = RestaurantHeat.objects.all()

     
        

        serializer = RestaurantHeatSerializer(
            restaurants, many=True, context={'request': request})
        return Response(serializer.data)



class RestaurantSerializer(serializers.ModelSerializer):
    """JSON serializer for games

    Arguments:
        serializer type
    """
    class Meta:
        model = Restaurant
        fields = ('id', 'name')


class RestaurantHeatSerializer(serializers.ModelSerializer):
    """JSON serializer for Restaurant heat levels
    

    Arguments:
        serializer type
    """
    restaurant = RestaurantSerializer(many=False)

    class Meta:
        model = RestaurantHeat
        url = serializers.HyperlinkedIdentityField(
            view_name='restaurant',
            lookup_field='id'
        )
        fields = ('id', 'name', 'restaurant', 'average_rating', 'ratings')
        depth = 1
