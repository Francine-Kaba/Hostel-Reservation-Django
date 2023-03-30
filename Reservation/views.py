from django.http import JsonResponse
from rest_framework.views import APIView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from Reservation.models import Room, Hostel, Floor, Block
from helpers.status_codes import UnavailableRoom, UnavailableFloor, UnavailableBlock, UnavailableHostel, NotAllowed, InvalidUser

# Create your views here.

"""
The Room class add a new room to a floor, into a block in a hostel into the database
"""
class RoomClass(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    # this function adds a new room to a floor in the hostel
    def post(self, request, *args, **kwargs):             
          # this if statement ensures that only a super admin and admin can add a room
        if self.request.user.role_id == 1 or self.request.user.role_id == 2:     
            name = request.data.get('name')
            number_of_persons = request.data.get('number_of_persons')
            is_available = request.data.get('is_available')
            price = request.data.get('price')
            floor_id = request.data.get('floor_id')
             # this try and catch ensures that we don't have the same room name on a particular floor
            try:
                Room.objects.get(name=name,floor_id=floor_id)     
                return JsonResponse({"message" : "Room name already exits, please change it"})
            except Room.DoesNotExist:
                # this try and catch ensures that the floor the room is being placed exists
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
            # this creates a room
            room = Room.objects.create(**details)                  
            data = Room.objects.filter(id=room.id).values()
            return JsonResponse({'message' : 'Room added successfully', 'data': list(data)})

        else:
            raise InvalidUser
        
    # The patch function update all details of the room in the database
    def patch(self, request, *args, **kwargs):    
        if self.request.user.role_id == 1 or self.request.user.role_id == 2:
            room_id = request.data.get('room_id')
            number_of_persons = request.data.get('number_of_persons')
            is_available = request.data.get('is_available')
            price = request.data.get('price')
            floor = request.data.get('floor_id')
            # this try ensures that the room being edited exists on the database
            try:                                 
                room = Room.objects.get(id=room_id)
            except Room.DoesNotExist:
                raise UnavailableRoom
            room.number_of_persons = number_of_persons
            room.is_available = is_available
            room.price = price
            room.floor_id = floor
            room.save()
            return JsonResponse({"message": "Room details changed successfully"})
        else:
            raise NotAllowed
        
    # The Delete function deletes a new room from the database
    def delete(self, request, *args, **kwargs):           
        room_id = request.data.get('room_id')
        try:
            room = Room.objects.get(id=room_id)
        except Room.DoesNotExist:
            raise UnavailableRoom('Unavailable, Room does not exist')
        if request.method == "DELETE":
            room.delete()
            return JsonResponse({'message' : 'Room deleted successfully'})
        else:
            return JsonResponse({'message' : 'Sorry, Unable to delete Room'})
        
     # The get function gets all the details of a specific room
    def get(self, request, *args, **kwargs):            
        room_id = request.data.get("room_id")
        try:
            Room.objects.get(id=room_id)
        except Room.DoesNotExist:
            raise UnavailableRoom
        data = Room.objects.filter(id=room_id).order_by("id").values('id', "name", "number_of_persons", "is_available", "price", "floor__gender", "floor__block", "floor__block__hostel")
        count = data.count()
        return JsonResponse({"detail": "success","data":list(data), "count": count})

    
"""
The Floor class add a new floor into a block, in a hostel into the database
"""
class FloorClass(APIView):                      
    authentication_classes = (IsAuthenticated,)
    permission_classes = (JWTAuthentication,)
    # this function adds a new floor to a block
    def post(self, request, *args, **kwargs):           
        # this if ensure only and admin or a super admin can add a floor            
        if self.request.user.role_id == 1 or self.request.user.role_id ==2:         
            name = request.data.get('name')
            gender = request.data.get('gender')
            block_id = request.data.get('block_id')
            # this try ensures that the block that the floor is being saved on exists
            try:                      
                Block.objects.get(id=block_id)
            except Block.DoesNotExist:
                raise UnavailableBlock('Unavailable, Block does not exist')
            details = {
                'name' : name,
                'gender' : gender,
                'block_id' : block_id
            }
            # this saves the floor on a block
            floor = Floor.objects.create(**details)      
            data = Floor.objects.filter(id=floor.id).values('id', 'name', 'gender', 'block_id')
            return JsonResponse({'message' : 'Floor added successfully', 'data': list(data)})
        
        else:
            raise InvalidUser
        
    # The patch function update all details of the floor in the database
    def patch(self, request, *args, **kwargs):    
        # this if ensure only and admin or a super admin can edit a floor
        if self.request.user.role_id == 1 or self.request.user.role_id == 2:         
            floor_id = request.data.get('floor_id')
            name = request.data.get('name')
            gender = request.data.get('gender')
            block = request.data.get('block')
            # this try ensures that the  floor is being edited exists
            try:                      
                floor = Floor.objects.get(id=floor_id)
            except Floor.DoesNotExist:
                raise UnavailableFloor
            floor.name = name
            floor.gender = gender
            floor.block = block
            floor.save()
            return JsonResponse({"message": "Floor details changed successfully"})
        else:
            raise NotAllowed
    
     # The Delete function deletes a new floor from the database
    def delete(self, request, *args, **kwargs):          
        floor_id = request.data.get('floor_id')
        # this try ensures that the  floor is being deleted exists
        try:                      
            floor = Floor.objects.get(id=floor_id)
        except Room.DoesNotExist:
            raise UnavailableFloor('Unavailable, Floor does not exist')
        if request.method == "DELETE":
            floor.delete()
            return JsonResponse({'message' : 'Floor deleted successfully'})
        else:
            return JsonResponse({'message' : 'Sorry, Unable to delete Floor'})

     # The get function gets all details of a specific floor
    def get(self, request, *args, **kwargs):            
        floor_id = request.data.get("floor_id")
        try:
            Floor.objects.get(id=floor_id)
        except Floor.DoesNotExist:
            raise UnavailableFloor
        data = Floor.objects.filter(id=floor_id).order_by("id").values('id', "name", "gender", "block_id", "block__hostel_id")
        count = data.count()
        return JsonResponse({"detail": "success","data":list(data), "count": count})
"""
The Block class add a new block into a hostel in the database
"""
class BlockClass(APIView):
    authentication_classes = (IsAuthenticated,)
    permission_classes = (JWTAuthentication,)

    # this function adds a new block to a hostel
    def post(self, request, *args, **kwargs):   
        # this if ensure only and admin or a super admin can add  a block                         
        if self.request.user.role_id == 1 or self.request.user.role_id ==2:         
            name = request.data.get('name')
            hostel_id = request.data.get('hostel_id')
            # this try ensures that the block that the hostel is being saved on exists
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
            return JsonResponse({'message' : 'Block added successfully', 'data': list(data)})
        else:
            raise InvalidUser('Invalid user, Not authorized')
    
    # The patch function update all details of the floor in the database
    def patch(self, request, *args, **kwargs):    
        # this if ensure only and admin or a super admin can edit a block
        if self.request.user.role_id == 1 or self.request.user.role_id == 2:         
            block_id = request.data.get('block_id')
            name = request.data.get('name')
            hostel = request.data.get('hostel')
            # this try ensures that the  floor is being edited exists
            try:                                  
                block = Block.objects.get(id=block_id)
            except Block.DoesNotExist:
                raise UnavailableBlock
            block.name = name
            block.hostel = hostel
            block.save()
            return JsonResponse({"message": "Block details changed successfully"})
        else:
            raise NotAllowed

    # The Delete function deletes a new block from the hostel in the database
    def delete(self, request, *args, **kwargs):          
        block_id = request.data.get('block_id')
        # this try ensures that the  block is being deleted exists
        try:                      
            block = Block.objects.get(id=block_id)
        except Block.DoesNotExist:
            raise UnavailableBlock('Unavailable, Block does not exist')
        if request.method == "DELETE":
            block.delete()
            return JsonResponse({'message' : 'Block deleted successfully'})
        else:
            return JsonResponse({'message' : 'Sorry, Unable to delete Block'})

    #The get function gets all details of a specific block
    def get(self, request, *args, **kwargs):                  
        block_id = request.data.get("block_id")
        try:
            Block.objects.get(id=block_id)
        except Block.DoesNotExist:
            raise UnavailableBlock
        data = Block.objects.filter(id=block_id).order_by("id").values('id', "name", "hostel__name")
        count = data.count()
        return JsonResponse({"detail": "success","data":list(data), "count": count})
"""
The Hostel class add a new hostel into the database
"""
class HostelClass(APIView):
    authentication_classes = (IsAuthenticated,)
    permission_classes = (JWTAuthentication,)

    # this function adds a new hostel into a system
    def post(self, request, *args, **kwargs):   
        # this if ensure only and admin or a super admin can add  a new hostel into the system          
        if self.request.user.role_id == 1 or self.request.user.role_id ==2:         
            name = request.data.get('name')
            hostel_image = request.data.get('hostel_image')
            contact = request.data.get('contact')
            hostel_type = request.data.get('hostel_type')
            # this try ensures that the hostel name that is being saved does not already exists
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
            return JsonResponse({'message' : 'Hostel added successfully', 'data': list(data)})
        else:
            raise InvalidUser('Invalid user, Not authorized')  

    # The patch function update all details of the hostel in the database
    def patch(self, request, *args, **kwargs):    
        # this if ensure only and admin or a super admin can edit  a  hostel in the system
        if self.request.user.role_id == 1 or self.request.user.role_id == 2:         
            hostel_id = request.data.get('hostel_id')
            name = request.data.get('name')
            hostel_image = request.data.get('hostel_image')
            hostel_type = request.data.get('hostel_type')
            block = request.data.get('block')
              # this try ensures that the  hostel is being edited exists
            try:                                
                hostel = Hostel.objects.get(id=hostel_id)
            except Hostel.DoesNotExist:
                raise UnavailableHostel
            hostel.name = name
            hostel.hostel_image = hostel_image
            hostel.hostel_type = hostel_type
            hostel.block = block
            hostel.save()
            return JsonResponse({"message": "Hostel details changed successfully"})
        else:
            raise NotAllowed
        
    # The DeleteHostel class deletes a new room from the database
    def delete(self, request, *args, **kwargs):         
        hostel_id = request.data.get('hostel_id')
        # this try ensures that the  hostel is being deleted exists
        try:                      
            hostel = Hostel.objects.get(id=hostel_id)
        except Hostel.DoesNotExist:
            raise UnavailableHostel
        if request.method == "DELETE":
            hostel.delete()
            return JsonResponse({'message' : 'Hostel deleted successfully'})
        else:
            return JsonResponse({'message' : 'Sorry, Unable to delete Hostel'})
        
    # The get function gets all details of a specific hostel
    def get(self, request, *args, **kwargs):                     
        hostel_id = request.data.get("hostel_id")
        try:
            Hostel.objects.get(id=hostel_id)
        except Hostel.DoesNotExist:
            raise UnavailableHostel
        data = Hostel.objects.filter(id=hostel_id).order_by("id").values('id', "name", "hostel_type", "contact", "hostel_image")
        count = data.count()
        return JsonResponse({"detail": "success","data":list(data), "count": count})
        

"""
The ListAllHostels class lists all hostels in the system and paginates the list.
"""
class ListAllHostels(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def get(self, request, *args, **kwargs):
        
        page_number = self.kwargs['page_number']

        response = 'Retrieved all hostels'
        hostels = Hostel.objects.filter().values('id', 'name', 'hostel_type', 'contact', 'hostel_image')

        data = Paginator(hostels, 5)
        # this try gets the page number
        try:         
           # returns the desired page object          
           page = data.get_page(page_number)  
           total = data.count  
           total_pages = data.num_pages  
        
           data = list(page)

           return JsonResponse({'status': 'success', 'detail': response, "current_page": page_number,"total_hostels": total, "total_pages": total_pages , "data" :data}, safe=False)
        except PageNotAnInteger:
           # if page_number is not an integer then assign the first page
           page = data.get_page(1)  # returns the desired page object
           total = data.count  
           total_pages = data.num_pages  

           data = list(page)

           return JsonResponse({'status': 'success', 'detail': response, "current_page": 1,"total_hostels": total, "total_pages": total_pages , "data" :data}, safe=False)
        except EmptyPage:
           # if page is empty then return last page
           page = data.page(data.num_pages)
           total = data.count  
           total_pages = data.num_pages  

           data = list(page)

           return JsonResponse({'status': 'success', 'detail': response, "current_page": data.num_pages,"total_hostels": total, "total_pages": total_pages , "data" :data}, safe=False)

"""
The GetAllHostelsRooms class gets a hostel in the system and all blocks, floors and rooms related to the hostel.
"""
class GetAllHostelsRooms(APIView):
    def get(self, request, *args, **kwargs):
        hostel_id = request.data.get("hostel_id")
         # this try ensures that the  hostel exists 
        try:                                         
            Hostel.objects.get(id=hostel_id)
        except Hostel.DoesNotExist:
            raise UnavailableHostel
        data = Room.objects.filter(floor__block__hostel=hostel_id).order_by("id").values('id', "name", "number_of_persons", "is_available", "price", "floor__id", "floor__gender", "floor__block", "floor__block__hostel")
        count = data.count()
        return JsonResponse({"detail": "success","data":list(data), "count": count})
    

"""
The GetAllRoomsGender class gets all rooms in the hostel according to the gender of the student
"""
class GetAllRoomsGender(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):

        gender = self.request.user.gender
        hostel_id = request.data.get("hostel_id")
        # this try ensures that the  hostel  exists
        try:                       
            Hostel.objects.get(id=hostel_id)
        except Hostel.DoesNotExist:
            raise UnavailableHostel
        data = Room.objects.filter(floor__block__hostel=hostel_id, floor__gender=gender).order_by("id").values('id', "name", "number_of_persons", "is_available", "price", "floor__id", "floor__gender", "floor__block", "floor__block__hostel")
        count = data.count()
        return JsonResponse({"detail": "success","data":list(data), "count": count})