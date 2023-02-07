from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from Authentication.models import User
from Reservation.models import Room, Hostel, Floor, Block
from helpers.status_codes import InvalidUser, UnavailableRoom, UnavailableFloor, UnavailableBlock, UnavailableHostel

# Create your views here.

"""
The Room class add a new room to a floor, into a block in a hostel into the database
"""
class RoomClass(APIView):
    # authentication_classes = (IsAuthenticated,)
    # permission_classes = (JWTAuthentication,)
    def post(self, request, *args, **kwargs):
        # if self.request.user.role_id == 1 or self.request.user.role_id ==2:
            name = request.data.get('name')
            floor_id = request.data.get('floor_id')
            try:
                Room.objects.get(name=name)
                return JsonResponse({"message" : "Room name already exixts, please change it"})
            except Room.DoesNotExist:
                try:
                 Floor.objects.get(id=floor_id)
                except Floor.DoesNotExist:
                    raise UnavailableFloor('Unavailable, Floor does not exist')
            details = {
                'name' : name,
                'floor_id' : floor_id
            }
            room = Room.objects.create(**details)
            data = Room.objects.filter(id=room.id).values('id', 'name', 'floor_id')
            return JsonResponse({'message' : 'Room added succesfully', 'data': list(data)})

        # else:
        #     raise InvalidUser('Invalid user, Not authorised')

    def delete(self, request, *args, **kwargs):           # The Delete function deletes a new room from the database
        room_id = request.data.get('room_id')
        try:
            room = Room.objects.get(id=room_id)
        except Room.DoesNotExist:
            raise UnavailableRoom('Unavailable, Room does not exist')
        if request.method == "DELETE":
            room.delete()
            return JsonResponse({'message' : 'Room deleted sucessfully'})
        else:
            return JsonResponse({'message' : 'Sorry, Unable to delete Room'})

    
"""
The Floor class add a new floor into a block, in a hostel into the database
"""
class FloorClass(APIView):
    # authentication_classes = (IsAuthenticated,)
    # permission_classes = (JWTAuthentication,)
    def post(self, request, *args, **kwargs):
        # if self.request.user.role_id == 1 or self.request.user.role_id ==2:
        name = request.data.get('name')
        block_id = request.data.get('block_id')
        try:
            Block.objects.get(id=block_id)
        except Block.DoesNotExist:
            raise UnavailableBlock('Unavailable, Block does not exist')
        details = {
            'name' : name,
            'block_id' : block_id
        }
        floor = Floor.objects.create(**details)
        data = Floor.objects.filter(id=floor.id).values('id', 'name', 'block_id')
        return JsonResponse({'message' : 'Floor added succesfully', 'data': list(data)})
      
        # else:
        #     raise InvalidUser('Invalid user, Not authorised')
    
    def delete(self, request, *args, **kwargs):           # The Delete function deletes a new floor from the database
        floor_id = request.data.get('floor_id')
        try:
            floor = Floor.objects.get(id=floor_id)
        except Room.DoesNotExist:
            raise UnavailableFloor('Unavailable, Floor does not exist')
        if request.method == "DELETE":
            floor.delete()
            return JsonResponse({'message' : 'Floor deleted sucessfully'})
        else:
            return JsonResponse({'message' : 'Sorry, Unable to delete Floor'})
"""
The Block class add a new block into a hostel in the database
"""
class BlockClass(APIView):
    # authentication_classes = (IsAuthenticated,)
    # permission_classes = (JWTAuthentication,)
    def post(self, request, *args, **kwargs):
        # if self.request.user.role_id == 1 or self.request.user.role_id ==2:
            name = request.data.get('name')
            hostel_id = request.data.get('hostel_id')
            try:
                Hostel.objects.get(id=hostel_id)
            except Hostel.DoesNotExist:
                raise UnavailableHostel('Unavailable, Hostel does not exist')
            details = {
                'name' : name,
                'hostel_id' : hostel_id
            }
            block = Block.objects.create(**details)
            data = Block.objects.filter(id=block.id).values('id', 'name', 'hostel_id')
            return JsonResponse({'message' : 'Block added succesfully', 'data': list(data)})
        # else:
        #     raise InvalidUser('Invalid user, Not authorised')

    def delete(self, request, *args, **kwargs):          # The Delete function deletes a new block from the database
        block_id = request.data.get('block_id')
        try:
            block = Block.objects.get(id=block_id)
        except Block.DoesNotExist:
            raise UnavailableBlock('Unavailable, Block does not exist')
        if request.method == "DELETE":
            block.delete()
            return JsonResponse({'message' : 'Block deleted sucessfully'})
        else:
            return JsonResponse({'message' : 'Sorry, Unable to delete Block'})
"""
The Hostel class add a new hostel into the database
"""
class HostelClass(APIView):
    # authentication_classes = (IsAuthenticated,)
    # permission_classes = (JWTAuthentication,)
    def post(self, request, *args, **kwargs):
        # if self.request.user.role_id == 1 or self.request.user.role_id ==2:
            name = request.data.get('name')
            try:
                Hostel.objects.get(name=name)
                return JsonResponse({"message" : "Hostel name already exists, please change the name"})
            except Hostel.DoesNotExist:
                 details = {
                'name' : name
            }
            hostel =Hostel.objects.create(**details)
            data = Hostel.objects.filter(id=hostel.id).values('id', 'name')
            return JsonResponse({'message' : 'Hostel added succesfully', 'data': list(data)})
        # else:
        #     raise InvalidUser('Invalid user, Not authorised')  
    
    def delete(self, request, *args, **kwargs):         # The DeleteHostel class deletes a new room from the database
        hostel_id = request.data.get('hostel_id')
        try:
            hostel = Hostel.objects.get(id=hostel_id)
        except Hostel.DoesNotExist:
            raise UnavailableHostel('Unavailable, Hostel does not exist')
        if request.method == "DELETE":
            hostel.delete()
            return JsonResponse({'message' : 'Hostel deleted sucessfully'})
        else:
            return JsonResponse({'message' : 'Sorry, Unable to delete Hostel'})

"""
The GetRoom class gets rooms from the database
"""
class GetRoom(APIView):
    def get(self, request, *args, **kwargs):
        data = Room.objects.values()
        count = data.count()
        return JsonResponse({"message": "success","data":list(data), "count": count})

"""
The GetFloor class gets rooms from the database
"""
class GetFloor(APIView):
    def get(self, request, *args, **kwargs):
        data = Floor.objects.values()
        count = data.count()
        return JsonResponse({"message": "success","data":list(data), "count": count})

"""
The GetBlock class gets rooms from the database
"""
class GetBlock(APIView):
    def get(self, request, *args, **kwargs):
        data = Block.objects.values()
        count = data.count()
        return JsonResponse({"message": "success","data":list(data), "count": count})

"""
The GetHostel class gets rooms from the database
"""
class GetHostel(APIView):
    def get(self, request, *args, **kwargs):
        data = Hostel.objects.values()
        count = data.count()
        return JsonResponse({"message": "success","data":list(data), "count": count})


