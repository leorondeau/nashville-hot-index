from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from nashvillehotindexapi.models import Order, restaurant, restaurantheat
from nashvillehotindexapi.models import Customer
from nashvillehotindexapi.models import Restaurant
from nashvillehotindexapi.models import RestaurantHeat



class Orders(ViewSet):

    def list(self, request):

        orders = Order.objects.all()

        serializer = OrderSerializer(
            orders, many=True, context={'request': request})
        
        return Response(serializer.data)

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id']

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name')

class RestaurantHeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantHeat
        fields = ['name']


class OrderSerializer(serializers.ModelSerializer):

    customer = CustomerSerializer(many=False) 
    restaurant= RestaurantSerializer(many=False)
    restaurantheat = RestaurantHeatSerializer(many=False)

    class Meta:
        model=Order
        url = serializers.HyperlinkedIdentityField(
            view_name='order',
            lookup_field='id'
        )
        fields = ('id', 'restaurant', 'customer', 'restaurantheat', 'note', 'enjoyable')
        depth = 1