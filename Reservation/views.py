from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from Reservation.models import Room, Hostel, Floor, Block
from helpers.status_codes import UnavailableRoom, UnavailableFloor, UnavailableBlock, UnavailableHostel, NotAllowed

# Create your views here.

"""
The Room class add a new room to a floor, into a block in a hostel into the database
"""
class RoomClass(APIView):
    # authentication_classes = (IsAuthenticated,)
    # permission_classes = (JWTAuthentication,)
    def post(self, request, *args, **kwargs):             # this function adds a new room to a floor
        # if self.request.user.role_id == 1 or self.request.user.role_id ==2:
            name = request.data.get('name')
            number_of_persons = request.data.get('number_of_persons')
            is_available = request.data.get('is_available')
            price = request.data.get('price')
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
                'number_of_persons' : number_of_persons,
                'is_available' : is_available,
                'price' : price,
                'floor_id' : floor_id
            }
            room = Room.objects.create(**details)
            data = Room.objects.filter(id=room.id).values()
            return JsonResponse({'message' : 'Room added succesfully', 'data': list(data)})

        # else:
        #     raise InvalidUser('Invalid user, Not authorised')
    def patch(self, request, *args, **kwargs):    # The patch function update all details of the room in the database
        # if self.request.user.role_id == 1 or self.request.user.role_id == 2:
            room_id = request.data.get('room_id')
            number_of_persons = request.data.get('number_of_persons')
            is_available = request.data.get('is_available')
            price = request.data.get('price')
            floor = request.data.get('floor_id')
            try:
                room = Room.objects.get(id=room_id)
            except Room.DoesNotExist:
                raise UnavailableRoom
            room.number_of_persons = number_of_persons
            room.is_available = is_available
            room.price = price
            room.floor_id = floor
            room.save()
            return JsonResponse({"message": "Room details changed sucessfully"})
        # else:
        #     raise NotAllowed

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

    def get(self, request, *args, **kwargs):                 # this function gets all rooms in the system
        data = Room.objects.values()
        count = data.count()
        return JsonResponse({"message": "success", "data":list(data), "count": count})

    
"""
The Floor class add a new floor into a block, in a hostel into the database
"""
class FloorClass(APIView):                      
    # authentication_classes = (IsAuthenticated,)
    # permission_classes = (JWTAuthentication,)
    def post(self, request, *args, **kwargs):                       # this function adds a new floor to a block
        # if self.request.user.role_id == 1 or self.request.user.role_id ==2:
        name = request.data.get('name')
        gender = request.data.get('gender')
        block_id = request.data.get('block_id')
        try:
            Block.objects.get(id=block_id)
        except Block.DoesNotExist:
            raise UnavailableBlock('Unavailable, Block does not exist')
        details = {
            'name' : name,
            'gender' : gender,
            'block_id' : block_id
        }
        floor = Floor.objects.create(**details)
        data = Floor.objects.filter(id=floor.id).values('id', 'name', 'gender', 'block_id')
        return JsonResponse({'message' : 'Floor added succesfully', 'data': list(data)})
      
        # else:
        #     raise InvalidUser('Invalid user, Not authorised')

    def patch(self, request, *args, **kwargs):    # The patch function update all details of the floor in the database
        # if self.request.user.role_id == 1 or self.request.user.role_id == 2:
            floor_id = request.data.get('floor_id')
            name = request.data.get('name')
            gender = request.data.get('gender')
            block = request.data.get('block')
            try:
                floor = Floor.objects.get(id=floor_id)
            except Floor.DoesNotExist:
                raise UnavailableFloor
            floor.name = name
            floor.gender = gender
            floor.block = block
            floor.save()
            return JsonResponse({"message": "Floor details changed sucessfully"})
        # else:
        #     raise NotAllowed
    
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

    def get(self, request, *args, **kwargs):                 # this function gets all floors in the system
        data = Floor.objects.values()
        count = data.count()
        return JsonResponse({"message": "success", "data":list(data), "count": count})

"""
The Block class add a new block into a hostel in the database
"""
class BlockClass(APIView):
    # authentication_classes = (IsAuthenticated,)
    # permission_classes = (JWTAuthentication,)
    def post(self, request, *args, **kwargs):                            # this function adds a new block to a hostel
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
        
    def patch(self, request, *args, **kwargs):    # The patch function update all details of the floor in the database
        # if self.request.user.role_id == 1 or self.request.user.role_id == 2:
            block_id = request.data.get('block_id')
            name = request.data.get('name')
            hostel = request.data.get('hostel')
            try:
                block = Block.objects.get(id=block_id)
            except Block.DoesNotExist:
                raise UnavailableBlock
            block.name = name
            block.hostel = hostel
            block.save()
            return JsonResponse({"message": "Block details changed sucessfully"})
        # else:
        #     raise NotAllowed

    def delete(self, request, *args, **kwargs):          # The Delete function deletes a new block from the hostel in the database
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

    def get(self, request, *args, **kwargs):                 # this function gets all blocks in the system
        data = Block.objects.values()
        count = data.count()
        return JsonResponse({"message": "success", "data":list(data), "count": count})
"""
The Hostel class add a new hostel into the database
"""
class HostelClass(APIView):
    # authentication_classes = (IsAuthenticated,)
    # permission_classes = (JWTAuthentication,)
    def post(self, request, *args, **kwargs):             # this function adds a new hostel into a system
        # if self.request.user.role_id == 1 or self.request.user.role_id ==2:
            name = request.data.get('name')
            hostel_image = request.data.get('hostel_image')
            contact = request.data.get('contact')
            hostel_type = request.data.get('hostel_type')
            try:
                Hostel.objects.get(name=name)
                return JsonResponse({"message" : "Hostel name already exists, please change the name"})
            except Hostel.DoesNotExist:
                 details = {
                'name' : name,
                'hostel_image' : hostel_image,
                'contact' : contact,
                'hostel_type' : hostel_type
            }
            hostel =Hostel.objects.create(**details)
            data = Hostel.objects.filter(id=hostel.id).values()
            return JsonResponse({'message' : 'Hostel added succesfully', 'data': list(data)})
        # else:
        #     raise InvalidUser('Invalid user, Not authorised')  

    def patch(self, request, *args, **kwargs):    # The patch function update all details of the hostel in the database
        # if self.request.user.role_id == 1 or self.request.user.role_id == 2:
            hostel_id = request.data.get('hostel_id')
            name = request.data.get('name')
            hostel_image = request.data.get('hostel_image')
            hostel_type = request.data.get('hostel_type')
            block = request.data.get('block')
            try:
                hostel = Hostel.objects.get(id=hostel_id)
            except Hostel.DoesNotExist:
                raise UnavailableHostel
            hostel.name = name
            hostel.hostel_image = hostel_image
            hostel.hostel_type = hostel_type
            hostel.block = block
            hostel.save()
            return JsonResponse({"message": "Hostel details changed sucessfully"})
        # else:
        #     raise NotAllowed
    
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

    def get(self, request, *args, **kwargs):                 # this function gets all hostels in the system
        page = request.GET.get('page')
        data = Hostel.objects.values()
        items = [data[i::5] for i in range(5)]
        print(data)
        count = data.count()
        return JsonResponse({"message": "success","data":items[int(page)], "count": count})
