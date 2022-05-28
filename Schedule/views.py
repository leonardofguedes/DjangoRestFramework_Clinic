from django.shortcuts import render
from rest_framework import viewsets
from Schedule.models import Room, Doctor
from Schedule.serializer import RoomSerializer, DoctorSerializer


class RoomViewSet(viewsets.ModelViewSet):  # já temos modelo vinculado, por isso usar o ModelViewSet
    queryset = Room.objects.all()  # indicará o queryset que utilizaremos
    serializer_class = RoomSerializer  # classe responsavel por serializar


class DoctorViewSet(viewsets.ModelViewSet):
    """Exibindo todos os países"""
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
