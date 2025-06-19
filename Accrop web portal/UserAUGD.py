
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
    Uid = json_data.get("id")
    print(Uid)
    print("UserCreatedSuccessfully.by code")
    return Uid 

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

# Disable User
def user_disable(id, remarks):
    url = base_url + "/user/disable"
    payload = {    
        "id": id,
        "remarks": remarks
    }
    response = requests.post(url, headers=headers, json=payload)
    assert response.status_code == 200, response.text 
    json_data = response.json()
    print("Disabled this user by Code.", json.dumps(json_data, indent=4))

# Enable User
def user_enable(id, remarks):
    url = base_url + "/user/enable"
    payload = {    
        "id": id,
        "remarks": remarks
    }
    response = requests.post(url, headers=headers, json=payload)
    assert response.status_code == 200, response.text 
    json_data = response.json()
    print("Enabled this user by code.", json.dumps(json_data, indent=4))


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
    
#get_user(Uid, 0, 10,"raj23@mathur.com")
# ------------------------------------------------------------




