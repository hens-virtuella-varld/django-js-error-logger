from rest_framework import serializers

from .models import JSError


class JSErrorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JSError
        fields = ['name', 'app_id', 'user', 'time', 'url', 'status', 'message', 'stack']
