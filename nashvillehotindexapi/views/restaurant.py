from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from nashvillehotindexapi.models import Restaurant
from nashvillehotindexapi.models import RestaurantHeat

from nashvillehotindexapi.models import Customer

class Restaurants(ViewSet):

    
    def retrieve(self, request, pk=None):
        """Handle GET requests for single game

        Returns:
            Response -- JSON serialized game instance
        """
        try:
            # `pk` is a parameter to this function, and
            # Django parses it from the URL route parameter
            #   http://localhost:8000/games/2
            #
            # The `2` at the end of he route becomes `pk
            
            restaurant = Restaurant.objects.get(pk=pk)
            customer = Customer.objects.get(user=request.auth.user)
            restaurant_heat_levels = RestaurantHeat.objects.filter(restaurant=restaurant)
            restaurant.suggested_heat = "mild"

            for heat_level in restaurant_heat_levels:
                if int(heat_level.average_rating) == (customer.heat_tolerance):
                    restaurant.suggested_heat = heat_level.name
                elif int(heat_level.average_rating) == (customer.heat_tolerance - 1):
                    restaurant.suggested_heat = heat_level.name
                elif int(heat_level.average_rating) == (customer.heat_tolerance + 1):
                    restaurant.suggested_heat = heat_level.name
                


            serializer = RestaurantSerializer(restaurant, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex, status=status.HTTP_404_NOT_FOUND) 
    
    def list(self, request):
        """Handle GET requests to games resource

        Returns:
            Response -- JSON serialized list of games
        """
        try:
            restaurants = Restaurant.objects.all()


            serializer = RestaurantSerializer(
                restaurants, many=True, context={'request': request})
            return Response(serializer.data)
        except ValueError as ex:
            return HttpResponseServerError(ex, status=status.HTTP_404_NOT_FOUND) 

    


class RestaurantSerializer(serializers.ModelSerializer):
    """JSON serializer for games

    Arguments:
        serializer type
    """
    class Meta:
        model = Restaurant
        url = serializers.HyperlinkedIdentityField(
            view_name='restaurant',
            lookup_field='id'
        )
        fields = ('id', 'name', 'website', 'img', 'heatlevels', 'suggested_heat')
        depth = 1

