from django.urls import path
from Reservation.views import HostelClass, BlockClass, FloorClass, RoomClass


urlpatterns = [
    path('room/',RoomClass.as_view(), name='room'),
    path('floor/',FloorClass.as_view(), name='floor'),
    path('block/',BlockClass.as_view(), name='block'),
    path('hostel/',HostelClass.as_view(), name='hostel'),  
]