from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from Reservation.models import Hostel, Block, Floor, Room
from helpers.status_codes import InvalidUser

# Create your views here.

"""
The AddRoom class add a new room to a floor, into a block in a hostel into the database
"""
class AddRoom(APIView):
    # authentication_classes = (IsAuthenticated,)
    # permission_classes = (JWTAuthentication,)
    def post(self, request, *args, **kwargs):
        # if self.request.user.role_id == 1 or self.request.user.role_id ==2:
            name = request.data.get('name')
            details = {
                'name' : name,
            }
            room = Room.objects.create(**details)
            data = Room.objects.filter(id=room.id).values('id', 'name')
            return JsonResponse({'message' : 'Room added succesfully', 'data': list(data)})
        # else:
        #     raise InvalidUser('Invalid user, Not authorised')
"""
The AddFloor class add a new floor into a block, in a hostel into the database
"""
class AddFloor(APIView):
    # authentication_classes = (IsAuthenticated,)
    # permission_classes = (JWTAuthentication,)
    def post(self, request, *args, **kwargs):
        # if self.request.user.role_id == 1 or self.request.user.role_id ==2:
            name = request.data.get('name')
            room = request.data.get('room')
            details = {
                    'name' : name,
                    'room_id' : room
            }
            floor = Floor.objects.create(**details)
            data = Floor.objects.filter(id=floor.id).values('id', 'name', 'room_id')
            return JsonResponse({'message' : 'Floor added succesfully', 'data': list(data)})
        # else:
        #     raise InvalidUser('Invalid user, Not authorised')

"""
The AddBlock class add a new block into a hostel in the database
"""
class AddBlock(APIView):
    # authentication_classes = (IsAuthenticated,)
    # permission_classes = (JWTAuthentication,)
    def post(self, request, *args, **kwargs):
        # if self.request.user.role_id == 1 or self.request.user.role_id ==2:
            name = request.data.get('name')
            floor = request.data.get('floor')
            details = {
                    'name' : name,
                    'floor_id' : floor
            }
            block = Block.objects.create(**details)
            data = Block.objects.filter(id=block.id).values('id', 'name', 'floor_id')
            return JsonResponse({'message' : 'Block added succesfully', 'data': list(data)})
        # else:
        #     raise InvalidUser('Invalid user, Not authorised')
"""
The AddHostel class add a new hostel into the database
"""
class AddHostel(APIView):
    # authentication_classes = (IsAuthenticated,)
    # permission_classes = (JWTAuthentication,)
    def post(self, request, *args, **kwargs):
        # if self.request.user.role_id == 1 or self.request.user.role_id ==2:
            name = request.data.get('name')
            block = request.data.get('block')
            details = {
                'name' : name,
                'block_id' : block
            }
            hostel =Hostel.objects.create(**details)
            data = Hostel.objects.filter(id=hostel.id).values('id', 'name', 'block_id')
            return JsonResponse({'message' : 'Hostel added succesfully', 'data': list(data)})
        # else:
        #     raise InvalidUser('Invalid user, Not authorised')

