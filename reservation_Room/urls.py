from django.urls import path
from .views import RoomsListView,ReservationsListView, RoomDetailView, RoomCreateView, RoomUpdateView, ReservationsCreateView, ReservationsUpdateView


urlpatterns = [
    path('rooms/',RoomsListView.as_view(),name='rooms_list'),
    path('rooms/<int:pk>',RoomDetailView.as_view(),name='detail_list'),
    path('rooms/create_room/',RoomCreateView.as_view(),name='create_room'),
    path('rooms/update_room/<int:pk>',RoomUpdateView.as_view(),name='update_room'),

    path('reservations/', ReservationsListView.as_view(),name='reservations_list'),
    path('reservations/create_reservations/', ReservationsCreateView.as_view(),name='create_reservations'),
    path('reservations/update_reservations/<int:pk>',ReservationsUpdateView.as_view(),name='update_reservations'),

] 