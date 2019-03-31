from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers

class HelloApiView(APIView):
    """ Test API View """

    serializer_class = serializers.HelloSerializers

    def get(self, request, format=None):
        """ Returns a lst of APIView features."""

        an_apivew = [
            'Uses HTTP method as function (get, post, patch, put, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'It mapped manually to URLs'
        ]

        return Response({'message': 'Hello','an_apiview': an_apivew})
    
    def post(self, request):
        """ Create a hello message with our name."""
        serializer = serializers.HelloSerializers(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {}'.format(name)

            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        """Handles updating an object."""
        
        return Response({'method': 'put'})


    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request."""

        return Response({'method':'patch'})


    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({'method':'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet."""

    def list(self, request):
        """Return a hello message."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functioanlity with less code.'
        ]

        return Response({'message':'Hello', 'a_viewset':a_viewset})

    def create(self, request):
        """Create a new hello message."""
        serializer = serializers.HelloSerializers(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "Hello {}".format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles getting an object by its ID."""

        return Response({'http_meth0d':'GET'})

    def update(self, request, pk=None):
        """Handles updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating part of an object. """
        return Response({'http_method': 'patch'})

    def destroy(self, request, pk=None):
        """handles removing an object."""
        return Response({'http_method': 'delete'})