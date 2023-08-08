from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Room,Reservation
from .serializers import RoomSerializer, RoomDetailSerializer, RoomCreateSerializer, RoomUpdateSerializer, ReservationSerializer, ReservationCreateSerializer, ReservationUpdateSerializer
from .permissions import OnlyAdmin


class RoomsListView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    Permission_classes = [AllowAny]

class RoomDetailView(RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer
    Permission_classes = [AllowAny]

class RoomCreateView(CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomCreateSerializer
    permission_classes = [IsAuthenticated & OnlyAdmin]

class RoomUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomUpdateSerializer
    permission_classes = [IsAuthenticated & OnlyAdmin]
    
class ReservationsListView(ListAPIView):
    
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.Is_employee:
            # Admins can see all reservations
            return Reservation.objects.all()
        else:
            # Regular users can see their own reservations
            return Reservation.objects.filter(user_ID=self.request.user)
    
class ReservationsCreateView(CreateAPIView):
    serializer_class = ReservationCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.Is_employee:
            # Admins can see all reservations
            return Reservation.objects.all()
        else:
            # Regular users can see their own reservations
            return Reservation.objects.filter(user_ID=self.request.user)

class ReservationsUpdateView(RetrieveUpdateDestroyAPIView):
    serializer_class = ReservationUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.Is_employee:
            # Admins can see all reservations
            return Reservation.objects.all()
        else:
            # Regular users can see their own reservations
            return Reservation.objects.filter(user_ID=self.request.user)
