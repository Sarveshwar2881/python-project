
import requests
import json  

base_url="https://70mzbzwmea.execute-api.ap-south-1.amazonaws.com"

auth_token="Bearer eyJraWQiOiJlYlZZOTl5XC8yK0ZoY0NHOFNyMFk2NSsrUWFwYitwWkxicksyWjNzOXFuWT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI0MTczOGRiYS02MGMxLTcwMWItYTA0OS00Y2QwMWFiYjMzZDQiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtc291dGgtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aC0xX2duSkJqWHFEQiIsImNsaWVudF9pZCI6IjRmaHQ5cjUwZnFrdGdxZjZxc2VraXRmYWlnIiwib3JpZ2luX2p0aSI6IjYyZjZkZTJiLWViMDMtNGNiYy1hZDI5LWVmMTRlNGNjZmM5OSIsImV2ZW50X2lkIjoiYTAyMTgwMmUtYTdhMi00OGQ4LWIwNWMtZjMwNGIwNzhlMTc5IiwidG9rZW5fdXNlIjoiYWNjZXNzIiwic2NvcGUiOiJhd3MuY29nbml0by5zaWduaW4udXNlci5hZG1pbiIsImF1dGhfdGltZSI6MTc0OTA5OTcyNSwiZXhwIjoxNzQ5MTg3MjY5LCJpYXQiOjE3NDkxMDA4NzAsImp0aSI6IjVmZDY0NzU2LWIwMDgtNDVlOC05MGNiLTE2MmQ5ZTIzMjdkMyIsInVzZXJuYW1lIjoiNDE3MzhkYmEtNjBjMS03MDFiLWEwNDktNGNkMDFhYmIzM2Q0In0.YCO2PPVC1dvIo62X33X3lXXmbEIwe6lCiQENMdh_y5l6HVKT8aQysafUTzMLuMv8YdVjDllJcR8rjxr0s01e92gOHJ-lbXkrtBpR0-uq299PRHm0lfj7juaX8JKK-pBLiKNyCnZJrt8X8o1uIZmVoys1fEYNGHOsWh6gcWZJdg2LUdUZ68yrDwIoYbVjyLxQ5XmDGjrG4MH-BXWYnTAPUhQfUrcASIg21KZ9BSiyChJ1uVpGZL7BIDMcG87H1MupkriALiSNiMrl6kLgNQV-aYbXo4jQGwzNblZBaySPZo8wIobKUTBMNpCY7Fhe1bbj17NNsnahLCiaAFb2w1Se-g"
def user_update():
    url = base_url +"/user/update"
    paylod={
    "role": 2,
    "email": "newuser001@test.com",
    "firstName": "Client",
    "id": "68401eca5bae83f2c9bdf833",
    "lastName": "001",
    "middleName": "Important",
    "phoneNumber": {
        "countryCode": "+91",
        "countryAlphaCode": "IN",
        "dialNumber": "1010101010"
    },
    # "departmentId": [],
    # "profileImage": [],   
    # "joiningDate": [],
    # "isContractor": []
}

    
    headers= {"Activerole":"2", "Authorization":auth_token}
    response = requests.post(url, headers = headers ,json=paylod)
    assert response.status_code == 200, response.text 
    json_data = response.json()
    print("UserUpdateSuccssfully.By Code." , json.dumps(json_data, indent=4))
user_update()

