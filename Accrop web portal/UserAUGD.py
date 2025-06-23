
import requests, json 
from URL import base_url, headers

# Add User
def user_create(role, email, firstName, lastName, middleName, countryCode, countryAlphaCode, dialNumber):
    url = base_url + "/user/add"
    payload = {                   
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
    
    response = requests.post(url, headers=headers, json=payload)
    assert response.status_code == 200, response.text 
    json_data = response.json()
    #print("UserCreatedSuccessfully.by Code." , json.dumps(json_data, indent=4))
    Uid = json_data.get("id") # Correct way to get 'id' from the JSON response
    print(Uid)
    print("User Created Successfully by code")
    return Uid
    
#Uid = user_create(2,"Raj2022@mathur.com","Raj","Kumar","Mathur","+91","IN",600000)

   
# Update User
def user_update(role, email, firstName, Uid, lastName, middleName, countryCode, countryAlphaCode, dialNumber):
    url = base_url + "/user/update"
    payload = {
        "role": role,
        "email": email,
        "firstName": firstName,
        "id": Uid,
        "lastName": lastName,
        "middleName": middleName,
        "phoneNumber": {
            "countryCode": countryCode,
            "countryAlphaCode": countryAlphaCode,
            "dialNumber": dialNumber
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    assert response.status_code == 200, response.text 
    print("UserUpdateSuccessfully.By Code.")

#user_update(2,"Raj2022@mathur.com","Change name Raj to Raja Ji","6858f28c7011d1815dad3ccf","change last Name New raja Ji","change middle Important","+91","IN","20001010")


# Disable User
def user_disable(Uid, remarks):
    url = base_url + "/user/disable"
    payload = {    
        "id": Uid,
        "remarks": remarks
    }
    response = requests.post(url, headers=headers, json=payload)
    assert response.status_code == 200, response.text 
    json_data = response.json()
    print("Disabled this user by Code.", json.dumps(json_data, indent=4))
    print(Uid)

#user_disable("6858f28c7011d1815dad3ccf", "Disabled by code.")

#Enable User
def user_enable(Uid, remarks):
    url = base_url + "/user/enable"
    payload = {    
        "id": Uid,
        "remarks": remarks
    }
    response = requests.post(url, headers=headers, json=payload)
    assert response.status_code == 200, response.text 
    json_data = response.json()
    print("Enabled this user by code.", json.dumps(json_data, indent=4))
    print(Uid)

#user_enable("6858f28c7011d1815dad3ccf", "Enabled by code.")


# Get Users
def get_user(Uid, skip, limit, Email):
    url = base_url +"/user/list"
    paylod={
    "customerId": Uid,
    "skip": skip,
    "limit": limit,
    "searchEmail": Email
}
    
    response = requests.post(url, headers = headers ,json=paylod)
    assert response.status_code == 200, response.text 
    json_data = response.json()
    print("json response body:" , json.dumps(json_data, indent=4))
    print(Uid)
    
# get_user("", 0, 10,"Raj2022@mathur.com")
# ------------------------------------------------------------




