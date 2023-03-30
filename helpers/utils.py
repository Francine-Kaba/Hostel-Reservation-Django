import re
from django.http import JsonResponse
from Authentication.models import Student
"""
Password validation regex
"""

def validate_password(password):
    response = {"status":True, "message": ""}
    capsletters_pattern = "(?=.*?[A-Z])"
    smallletters_pattern = "(?=.*?[a-z])"           
    numbers_pattern = "(?=.*?[0-9])"           
    specialletters_pattern = "(?=.*?[#?!@$%^&*-])"           
    min_len_pattern = ".{8,}$"
    
    if re.match(min_len_pattern, password) is None:
        response["message"] = "Password is less than 8 characters"
        response["status"] = False
        return response       
    if re.match(specialletters_pattern, password) is None:
        response["message"] = "Password must contain Special characters eg. @#$&*()"
        response["status"] = False
        return response  
    if re.match(capsletters_pattern, password) is None:
        response["message"] = "Password must contain Upper case letter or characters"
        response["status"] = False
        return response     
    if re.match(smallletters_pattern, password) is None:
        response["message"] = "Password must contain small case letters or characters"
        response["status"] = False
        return response  
    if re.match(numbers_pattern, password) is None:
        response["message"] = "Password must contain numbers"
        response["status"] = False
        return response         

    return response
"""
Email validation regex
"""
def validate_email(email):
    response = {"status": True, "detail": ""}

    email_pattern = "^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"

    if re.match(email_pattern, email) is None:
        response["detail"] = "Email is not valid"
        response["status"] = False
        return response
    
    return response
"""
Name validation regex
"""
def validate_name(string):
    response = {"status": True, "detail": ""}
    string_pattern = r"^[\-'a-zA-Z ]+$"
    if not string:
        response["detail"] = "Field cannot be empty"
        response["status"] = False
        return response
    
    if re.match(string_pattern, string) is None:
        response["detail"] = "Illegal Input"
        response["status"] = False
        return response
    
    if string.isspace():
        response["detail"] = "Only characters can be entered"
        response["status"] = False
        return response

    
    return response
"""
Validation regex
"""
def validate_user_input(email, first_name, last_name, password):
    validation_errors = []
    
    if not validate_email(email)["status"]:
        validation_errors.append(validate_email(email)["detail"])
        
    if not validate_name(first_name)["status"]:
        validation_errors.append(validate_name(first_name)["detail"])

    if not validate_name(last_name)["status"]:
        validation_errors.append(validate_name(last_name)["detail"])
        
    if not validate_password(password)["status"]:
        validation_errors.append(validate_password(password)["detail"])
    
    if validation_errors:
        return JsonResponse({"detail": ", ".join(validation_errors)}, status=433)
    else:
        return None
    
"""
Login Validation regex
"""
def validate_login_user_input(email, password):
    validation_errors = []
    
    if not validate_email(email)["status"]:
        validation_errors.append(validate_email(email)["detail"])
        
    if not validate_password(password)["status"]:
        validation_errors.append(validate_password(password)["detail"])
    
    if validation_errors:
        return JsonResponse({"detail": ", ".join(validation_errors)}, status=433)
    else:
        return None

"""
Signup Validation function
"""
# def signup_validation (email, student_id, phone_number, faculty, program):
   