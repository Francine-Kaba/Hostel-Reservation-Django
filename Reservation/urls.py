from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from Reservation.views import (HostelClass, BlockClass, FloorClass, RoomClass, ListAllHostels, GetAllHostelsRooms, GetAllRoomsGender)


urlpatterns = [
    path('room/',RoomClass.as_view(), name='room'),
    path('floor/',FloorClass.as_view(), name='floor'),
    path('block/',BlockClass.as_view(), name='block'),
    path('hostel/',HostelClass.as_view(), name='hostel'),  
    path('list-all-hostels/<int:page_number>/',ListAllHostels.as_view(), name='list-all-hostels'),  
    path('get-all-hostel-rooms/',GetAllHostelsRooms.as_view(), name='get-all-hostel-rooms'),  
    path('get-all-rooms-gender/', GetAllRoomsGender.as_view(), name='get-all-rooms-gender'),  



]





urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)