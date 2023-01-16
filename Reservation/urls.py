from django.urls import path
from Reservation.views import AddHostel, AddBlock, AddFloor, AddRoom


urlpatterns = [
    path('add-room/',AddRoom.as_view(), name='add-room'),
    path('add-floor/',AddFloor.as_view(), name='add-floor'),
    path('add-block/',AddBlock.as_view(), name='add-block'),
    path('add-hostel/',AddHostel.as_view(), name='add-hostel'),   
]