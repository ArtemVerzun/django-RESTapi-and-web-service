from rest_framework import serializers
from .models import User, Event


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class UserSerializer2(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'login']


class EventSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id']

