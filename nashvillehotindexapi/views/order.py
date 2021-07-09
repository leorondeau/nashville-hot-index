import re
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from nashvillehotindexapi.models import Order
from nashvillehotindexapi.models import Customer
from nashvillehotindexapi.models import Restaurant
from nashvillehotindexapi.models import RestaurantHeat
from nashvillehotindexapi.models import Rating
from django.core.paginator import Paginator




class Orders(ViewSet):

    def create(self, request):
        """Handle POST operations for Orders

        Returns:
            Response -- JSON serialized event instance
        """
        customer = Customer.objects.get(user=request.auth.user)

        order = Order()
        order.note = request.data["note"]
        order.enjoyable = request.data["enjoyable"]
        order.created_date = request.data["createdDate"]
        order.customer = customer

        restaurant = Restaurant.objects.get(pk=request.data["restaurantId"])
        restaurantheat = RestaurantHeat.objects.get(pk=request.data["restaurantHeatId"])
        
        order.restaurant = restaurant
        order.restaurantheat = restaurantheat

       

        try:
            order.save()
            rating = Rating()
            rating.restaurantheat = restaurantheat
            rating.order = order
            rating.rating = request.data["rating"]
            rating.save()
            
            return Response({"message": "Rating added"}, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

        


    def update(self, request, pk=None):
        """Handle POST operations for Orders

        Returns:
            Response -- JSON serialized event instance
        """
        customer = Customer.objects.get(user=request.auth.user)

        order = Order.objects.get(pk=pk)
        order.note = request.data["note"]
        order.enjoyable = request.data["enjoyable"]
        order.customer = customer
        
        restaurant = Restaurant.objects.get(pk=request.data["restaurantId"])
        restaurantheat = RestaurantHeat.objects.get(pk=request.data["restaurantHeatId"])
        rating = Rating.objects.get(order_id=order.id)

        rating.rating = request.data["rating"]
        rating.save()
        order.restaurant = restaurant
        order.restaurantheat = restaurantheat
        order.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single game

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            order = Order.objects.get(pk=pk)
            order.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)
 
        except Order.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):

        

        try:

            order = Order.objects.get(pk=pk)
            rating = Rating.objects.get(order_id = order.id)
            order.rating = rating
            order.save()
            serializer = OrderSerializer(
            order, context={'request': request})        
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request, pk=None):

        
        
        customer = Customer.objects.get(user=request.auth.user)
        orders = Order.objects.filter(customer__id = customer.id ).order_by('-id')
        restaurant = self.request.query_params.get('restaurantid', None)
        limit = self.request.query_params.get('limit', None)
        
        if restaurant is not None:
            if limit is not None:

                orders = orders.filter(
                    restaurant__id = restaurant,
                    customer__id = customer.id
                )[:int(limit)]
            else:
                orders = orders.filter(
                    restaurant__id = restaurant,
                    customer__id = customer.id)
        else:
            if limit is not None:

                orders = orders.filter(
                   
                    customer__id = customer.id
                )[:int(limit)]
            else:
                orders = orders.filter(
                    
                    customer__id = customer.id)

        serializer = OrderListSerializer(
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
        fields = ('id','name')
        depth = 1

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id','rating')

class OrderSerializer(serializers.ModelSerializer):

    customer = CustomerSerializer(many=False) 
    restaurant= RestaurantSerializer(many=False)
    restaurantheat = RestaurantHeatSerializer(many=False)
    rating = RatingSerializer(many=False)

    class Meta:
        model=Order
        url = serializers.HyperlinkedIdentityField(
            view_name='order',
            lookup_field='id'
        )
        fields = ('id', 'restaurant', 'customer', 
        'restaurantheat', 'note', 'enjoyable', 'rating')
        depth = 1

class OrderListSerializer(serializers.ModelSerializer):

    customer = CustomerSerializer(many=False) 
    restaurant= RestaurantSerializer(many=False)
    restaurantheat = RestaurantHeatSerializer(many=False)
    

    class Meta:
        paginate_by=2
        model=Order
        url = serializers.HyperlinkedIdentityField(
            view_name='order',
            lookup_field='id'
        )
        fields = ('id', 'restaurant', 'customer', 
        'restaurantheat', 'note', 'enjoyable')
        depth = 1