from django.shortcuts import render
from producers.user_created import ProducerUserCreated
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
import json
# Create your views here.

producerUserCreated = ProducerUserCreated()


class RegisterView(APIView):
    def get(self, request):
        producerUserCreated.publish("user_created_method", json.dumps({
            'email': "jugalchanda7@gmail.com"
        }))
        return Response({"message": "Hello, World!"})
