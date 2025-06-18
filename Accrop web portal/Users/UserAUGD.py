import requests  
import json  
from URL import base_url, headers

# Add User
def user_create(role, email, firstName, lastName, middleName, countryCode, countryAlphaCode, dialNumber):
    url = base_url +"/user/add"
    payload={                   
    "role": role,
    "email": email,
    "firstName": firstName,
    "lastName": lastName,
    "middleName": middleName,
    "phoneNumber": {
        "countryCode": countryCode,
        "countryAlphaCode": countryAlphaCode,
        "dialNumber": dialNumber
    },
}
    response = requests.post(url, headers = headers ,json=payload)
    assert response.status_code == 200, response.text  
    json_data = response.json()
    id = json_data.get(id)
    print(id)
    print("UserCreatedSuccessfully.by code", json.dumps(json_data, indent=4))

    return id
   

    
#user_create(4,"Raj04@mathur.com","Raj","Kumar","Mathur","+91","IN",64664646)


# Update User
def user_update(role, email, firstName, id, lastName, middleName, countryCode, countryAlphaCode, dialNumber):
    url = base_url +"/user/update"
    paylod={
    "role": role,
    "email": email,
    "firstName": firstName,
    "id": id,
    "lastName": lastName,
    "middleName": middleName,
    "phoneNumber": {
        "countryCode":countryCode,
        "countryAlphaCode": countryAlphaCode,
        "dialNumber": dialNumber,
    }
}
    
    response = requests.post(url, headers = headers ,json=paylod)
    assert response.status_code == 200, response.text 
    json_data = response.json()
    print("UserUpdateSuccssfully.By Code.", json.dumps(json_data, indent=4))

#user_update(2,"raj04@mathur.com","NewRaj004",id,"NewMathur004","Important","+91","IN","20001010")




# Enable User
def user_enable(id,remarks):
    url = base_url +"/user/enable"
    paylod={    
    "id": id,
    "remarks": remarks
}
   
    response = requests.post(url, headers = headers ,json=paylod)
    assert response.status_code == 200, response.text 
    json_data = response.json()
    print("Enabeled this user by code." , json.dumps(json_data, indent=4))

#user_enable("id","Enabaled by code.")




