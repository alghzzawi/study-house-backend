from rest_framework import serializers
from .models import Room,Reservation

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields='__all__'

class RoomDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields='__all__'

class RoomCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields='__all__'

class RoomUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields='__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields='__all__'

class ReservationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields='__all__'

class ReservationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields='__all__'