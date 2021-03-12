from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from nashvillehotindexapi.models import Restaurant

class Restaurants(ViewSet):

    def list(self, request):
        """Handle GET requests to games resource

        Returns:
            Response -- JSON serialized list of games
        """
        # Get all game records from the database
        restaurants = Restaurant.objects.all()

        # Support filtering games by type
        #    http://localhost:8000/games?type=1
        #
        # That URL will retrieve all tabletop games
        

        serializer = RestaurantSerializer(
            restaurants, many=True, context={'request': request})
        return Response(serializer.data)


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
        fields = ('id', 'name', 'website', 'img')
        depth = 1

