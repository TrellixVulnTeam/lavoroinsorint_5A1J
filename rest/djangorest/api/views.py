from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import BucketlistSerializer
from .models import Bucketlist

class CreateView(generics.ListCreateAPIView):

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        serializer.save()
