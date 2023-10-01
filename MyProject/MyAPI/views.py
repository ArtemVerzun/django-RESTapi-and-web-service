import json

from django.http import Http404, HttpResponse
from django.shortcuts import render
from rest_framework import generics
from .models import User, Event
from .serializers import UserSerializer, EventSerializer, UserSerializer2, EventSerializer2
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view


# создание пользователя
class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Авторизация--------------------------
class UserLoginView(APIView):
    def get(self, request, login, password):
        if request.method == 'GET':
            obj = User.objects.filter(login=login, password=password)
            serializer = UserSerializer(obj, many=True)
            return Response(serializer.data, status=200)


# создание события
class EventCreateView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


# просмотр событий
class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


# получение конкретного события и его изменение
class AddRecordView(APIView):
    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = EventSerializer(obj)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = EventSerializer(obj, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.data, status=400)

    def put(self, request, pk, format=None):

        obj = self.get_object(pk)
        serializer = EventSerializer(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.data, status=400)


# получение конкретного события для отображения в разделе мои события
class FindCreator(APIView):
    def get(self, request, creator):
        if request.method == 'GET':
            obj = Event.objects.filter(creator=creator)
            serializer = EventSerializer(obj, many=True)
            list_of_dicts = [dict(item) for item in serializer.data]
            answer = json.dumps(serializer.data[0], ensure_ascii=False)
            return Response(serializer.data, status=200)


# получение инфы о пользователе по id
class ListUserInfo(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = UserSerializer(obj)
        return Response(serializer.data)


# получение инфы о пользователе по логину
class ListUserInfo2(APIView):
    def get_object(self, login):
        try:
            return User.objects.get(login=login)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, login, format=None):
        obj = self.get_object(login)
        serializer = UserSerializer(obj)
        return Response(serializer.data)


# удаление события
class EventDeleteView(generics.DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


