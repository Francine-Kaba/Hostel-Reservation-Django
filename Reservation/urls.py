from django.urls import path
from Reservation.views import HostelClass, BlockClass, FloorClass, RoomClass,  GetRoom, GetFloor, GetBlock, GetHostel


urlpatterns = [
    path('add-room/',RoomClass.as_view(), name='add-room'),
    path('add-floor/',FloorClass.as_view(), name='add-floor'),
    path('add-block/',BlockClass.as_view(), name='add-block'),
    path('add-hostel/',HostelClass.as_view(), name='add-hostel'),  
    path('get-room/',GetRoom.as_view(), name='get-room'),  
    path('get-floor/',GetFloor.as_view(), name='get-floor'),  
    path('get-block/',GetBlock.as_view(), name='get-block'),  
    path('get-hostel/',GetHostel.as_view(), name='get-hostel'),  
]