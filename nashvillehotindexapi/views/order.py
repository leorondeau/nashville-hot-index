import re
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

    def create(self, request):
        """Handle POST operations for Orders

        Returns:
            Response -- JSON serialized event instance
        """
        customer = Customer.objects.get(user=request.auth.user)

        order = Order()
        order.note = request.data["note"]
        order.customer = customer["customerId"]
        order.enjoyable = request.data["enjoyable"]

        restaurant = Restaurant.objects.get(pk=request.data["restaurantId"])
        restaurantheat = RestaurantHeat.objects.get(pk=request.data["restaurantHeatId"])
        
        order.restaurant = restaurant
        order.restaurantheat = restaurantheat

        try:
            order.save()
            serializer = OrderSerializer(order, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)



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