from rest_framework.exceptions import APIException

class CannotSendMail(APIException):
    status_codes = 432
    default_detail = 'Cannot send mail'

class NotAllowed(APIException):
    status_codes = 433
    default_detail = "Action not allowed"

class UserAlreadyExist(APIException):
    status_codes = 434
    default_detail = "User already exists"

class RoleDoesNotExist(APIException):
    status_codes = 435
    default_detail = 'Role Does Not Exist'

class ChangePassword(APIException):
    status_codes = 436
    default_detail = "Please change your password"

class UserDoesNotExist(APIException):
    status_codes = 437
    default_detail = 'User Does Not Exist'

class InvalidPassword(APIException):
    status_code = 438
    default_detail = 'Invalid Password, Use the correct password'
    default_code = 'Invalid Password'

class WrongCredentials(APIException):
    status_codes = 439
    default_detail = 'Wrong Credentials, Use the correct credentials'
    default_code = 'Wrong Credentials'

class WrongToken(APIException):
    status_codes = 440
    default_detail = 'Wrong Token, use correct token'
    
class InvalidUser(APIException):
    status_codes = 441
    default_detail = 'Invalid user, Not authorised'

class UnavailableRoom(APIException):
    status_codes = 442
    default_detail = 'Unavailable, Room does not exist'

class UnavailableFloor(APIException):
    status_codes = 443
    default_detail = 'Unavailable, Floor does not exist'

class UnavailableBlock(APIException):
    status_codes = 444
    default_detail = 'Unavailable, Block does not exist'

class UnavailableHostel(APIException):
    status_codes = 445
    default_detail = 'Unavailable, Hostel does not exist'
