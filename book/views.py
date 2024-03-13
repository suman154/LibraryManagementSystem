from django.shortcuts import render
from rest_framework import ModelViewSet
from rest_framework import GroupSerializer
from rest_framework import AllowAny


# Create your views here.
class GroupView(ModelViewSet):
    serislizer_class = GroupSerializer
    permession_classes = [AllowAny]


