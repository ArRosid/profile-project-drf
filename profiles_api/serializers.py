from rest_framework import serializers

from . import models

class HelloSerializers(serializers.Serializer):
    """Serializers a name field for testing our APIView"""

    name = serializers.CharField(max_length=10) 