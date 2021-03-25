import re
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.models import User
from nashvillehotindexapi.models import Customer


class Profile(ViewSet):
    """customer can see profile information"""

    def list(self, request):
        """Handle GET requests to profile resource

        Returns:
            Response -- JSON representation of user info and events
        """
        customer = Customer.objects.get(user=request.auth.user)
        

    
        customer = CustomerSerializer(
            customer, many=False, context={'request': request})

        # Manually construct the JSON structure you want in the response
        profile = {}
        profile["customer"] = customer.data


        return Response(profile)

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for customer's related Django user"""
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')


class CustomerSerializer(serializers.ModelSerializer):
    """JSON serializer for customers"""
    user = UserSerializer(many=False)

    class Meta:
        model = Customer
        fields = ('user', 'heat_tolerance')
