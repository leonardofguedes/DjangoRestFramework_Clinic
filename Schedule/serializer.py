from rest_framework import serializers
from Schedule.models import Room, Doctor


class RoomSerializer(serializers.ModelSerializer):
    class Meta:  # qual o modelo e os campos que utilizaremos
        model = Room
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'