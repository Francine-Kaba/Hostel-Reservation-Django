import re

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