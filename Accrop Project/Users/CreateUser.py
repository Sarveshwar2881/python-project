
# import requests # 
# import json  # For data will be appered on json fome.

# base_url="https://70mzbzwmea.execute-api.ap-south-1.amazonaws.com" # All API will be hit on this URL.

# auth_token="Bearer eyJraWQiOiJlYlZZOTl5XC8yK0ZoY0NHOFNyMFk2NSsrUWFwYitwWkxicksyWjNzOXFuWT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI0MTczOGRiYS02MGMxLTcwMWItYTA0OS00Y2QwMWFiYjMzZDQiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtc291dGgtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aC0xX2duSkJqWHFEQiIsImNsaWVudF9pZCI6IjRmaHQ5cjUwZnFrdGdxZjZxc2VraXRmYWlnIiwib3JpZ2luX2p0aSI6ImIyZmE1ZTMxLTZkODYtNDYwNi05OTE4LWJlMDFmZTE0MGZiNiIsImV2ZW50X2lkIjoiYzU4OWE1NTEtYzU5Ni00NjQ4LTk2YWItZTFjNThlNjc0NTAxIiwidG9rZW5fdXNlIjoiYWNjZXNzIiwic2NvcGUiOiJhd3MuY29nbml0by5zaWduaW4udXNlci5hZG1pbiIsImF1dGhfdGltZSI6MTc0OTAyOTg0NCwiZXhwIjoxNzQ5MTE3ODk0LCJpYXQiOjE3NDkwMzE0OTQsImp0aSI6ImQ3N2Y5M2VkLTIxZTctNDNjNi1iYmMzLWE4OWMyYzZjMjk2ZCIsInVzZXJuYW1lIjoiNDE3MzhkYmEtNjBjMS03MDFiLWEwNDktNGNkMDFhYmIzM2Q0In0.liKI26g4gu3N7iJYf_Is1P0hmfmJ_wQTaMuUSt-kmIPb7_0eUx6D2pNwiERBMx7PvdSImRg81EI4PKvXClBXNAJotXZU7rHQ66xrQBhyvL9fEtULWX0ovWOkkA-MzI4X0lNwMFLu8_RlYo1G9P1NOuAl4gom4o3Pg3Uh1hUEGm_vx6sz1RPvoJscWPtXyPiKEdIzP6mhIugqwneb-WixPIcyiQUOOvZZoKwYbesdu2vOiZpgJJbxRlDqvQmSJkQk3P3otVpI4uNKqdJj90rSLVk8b6J2eqqAlQS6briNVEyebnCWvX4U8eOJHXHPxd1n-dKsenupPzwlRPUBIdFmZg" # ye yehe batata hai ki kya kerna hai.
# def user_create(role,email,firstName,lastName,middleName,phoneNumber,countryCode,countryAlphaCode,dialNumber):
#     url = base_url +"/user/add"
#     paylod={                    # Payload a type of disneary in which all parameter is appeard for api hit.
#     # "role": 31,
#     # "email": "newuser008@test.com",
#     # "firstName": "New",
#     # "lastName": "User",
#     # "middleName": "001",
#     # "phoneNumber": {
#     #     "countryCode": "+91",
#     #     "countryAlphaCode": "IN",
#     #     "dialNumber": "1010101010"
#     },

#     # "joiningDate": null,
#     # "isContractor": false
#     # header --पाइथन में, किसी भी मॉड्यूल को शुरू करने के लिए आप एक हेडर लिख सकते हैं। इस हेडर में आप उस मॉड्यूल के बारे में जानकारी, जैसे कि लेखक, संस्करण, और कोई और जानकारी दे सकते हैं।
#     # Response == जब आप पायथन में किसी सर्वर या API पर एक अनुरोध भेजते हैं, तो सर्वर या API आपको एक प्रतिक्रिया भेजता है, जिसे रिस्पांस कहा जाता है. 2)जब आप किसी API पर अनुरोध भेजते हैं, तो API आपको एक API रिस्पांस भेजता है, जो आमतौर पर JSON डेटा या अन्य प्रारूप में होता है.
# }
    
#     headers = {"Activerole":"2", "Authorization":auth_token}
#     response = requests.post(url, headers = headers ,json=paylod)
#     assert response.status_code == 200, response.text  # assert Result delear kerta hai.
#     json_data = response.json()
#     print("UserCreatedSuccessfully.by Code." , json.dumps(json_data, indent=4))

# user_create(2,Raj@mathur.com,Raj,Kumar,Mathur,01122321668,91,IN,9718899143)  # ye fuction ko call kerta hai.






# import requests  
# import json  

# base_url="https://70mzbzwmea.execute-api.ap-south-1.amazonaws.com" 

# auth_token="Bearer eyJraWQiOiJlYlZZOTl5XC8yK0ZoY0NHOFNyMFk2NSsrUWFwYitwWkxicksyWjNzOXFuWT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI0MTczOGRiYS02MGMxLTcwMWItYTA0OS00Y2QwMWFiYjMzZDQiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtc291dGgtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aC0xX2duSkJqWHFEQiIsImNsaWVudF9pZCI6IjRmaHQ5cjUwZnFrdGdxZjZxc2VraXRmYWlnIiwib3JpZ2luX2p0aSI6ImIyZmE1ZTMxLTZkODYtNDYwNi05OTE4LWJlMDFmZTE0MGZiNiIsImV2ZW50X2lkIjoiYzU4OWE1NTEtYzU5Ni00NjQ4LTk2YWItZTFjNThlNjc0NTAxIiwidG9rZW5fdXNlIjoiYWNjZXNzIiwic2NvcGUiOiJhd3MuY29nbml0by5zaWduaW4udXNlci5hZG1pbiIsImF1dGhfdGltZSI6MTc0OTAyOTg0NCwiZXhwIjoxNzQ5MTE3ODk0LCJpYXQiOjE3NDkwMzE0OTQsImp0aSI6ImQ3N2Y5M2VkLTIxZTctNDNjNi1iYmMzLWE4OWMyYzZjMjk2ZCIsInVzZXJuYW1lIjoiNDE3MzhkYmEtNjBjMS03MDFiLWEwNDktNGNkMDFhYmIzM2Q0In0.liKI26g4gu3N7iJYf_Is1P0hmfmJ_wQTaMuUSt-kmIPb7_0eUx6D2pNwiERBMx7PvdSImRg81EI4PKvXClBXNAJotXZU7rHQ66xrQBhyvL9fEtULWX0ovWOkkA-MzI4X0lNwMFLu8_RlYo1G9P1NOuAl4gom4o3Pg3Uh1hUEGm_vx6sz1RPvoJscWPtXyPiKEdIzP6mhIugqwneb-WixPIcyiQUOOvZZoKwYbesdu2vOiZpgJJbxRlDqvQmSJkQk3P3otVpI4uNKqdJj90rSLVk8b6J2eqqAlQS6briNVEyebnCWvX4U8eOJHXHPxd1n-dKsenupPzwlRPUBIdFmZg" 
# def user_create(role,email,firstName,lastName,middleName,phoneNumber,countryCode,countryAlphaCode,dialNumber):
#     url = base_url +"/user/add"
#     paylod={                   
#     # "role": 31,
#     # "email": "newuser008@test.com",
#     # "firstName": "New",
#     # "lastName": "User",
#     # "middleName": "001",
#     # "phoneNumber": {
#     #     "countryCode": "+91",
#     #     "countryAlphaCode": "IN",
#     #     "dialNumber": "1010101010"
#     },
# }
    
#     headers = {"Activerole":"2", "Authorization":auth_token}
#     response = requests.post(url, headers = headers ,json=paylod)
#     assert response.status_code == 200, response.text  # assert Result delear kerta hai.
#     json_data = response.json()
#     print("UserCreatedSuccessfully.by Code." , json.dumps(json_data, indent=4))

# user_create(2,Raj@mathur.com,Raj,Kumar,Mathur,01122321668,91,IN,9718899143)  


import requests  
import json  

base_url="https://70mzbzwmea.execute-api.ap-south-1.amazonaws.com" 

auth_token="Bearer eyJraWQiOiJlYlZZOTl5XC8yK0ZoY0NHOFNyMFk2NSsrUWFwYitwWkxicksyWjNzOXFuWT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI0MTczOGRiYS02MGMxLTcwMWItYTA0OS00Y2QwMWFiYjMzZDQiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtc291dGgtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aC0xX2duSkJqWHFEQiIsImNsaWVudF9pZCI6IjRmaHQ5cjUwZnFrdGdxZjZxc2VraXRmYWlnIiwib3JpZ2luX2p0aSI6IjhhMzExOTgxLWQ5MjQtNDE0NC1iOTc4LTE1MmM2YjVmZjQwNSIsImV2ZW50X2lkIjoiNDljN2Y3ZmItN2E5ZC00M2Q3LTg4YWYtZmExMGY2OTkwZTdiIiwidG9rZW5fdXNlIjoiYWNjZXNzIiwic2NvcGUiOiJhd3MuY29nbml0by5zaWduaW4udXNlci5hZG1pbiIsImF1dGhfdGltZSI6MTc0OTcwODYxNiwiZXhwIjoxNzQ5ODA0Mjg3LCJpYXQiOjE3NDk3MTc4ODcsImp0aSI6ImIwNWU1MGEyLWVmYjAtNDAwMi04NDAyLTdhODBlZDU3N2ViMCIsInVzZXJuYW1lIjoiNDE3MzhkYmEtNjBjMS03MDFiLWEwNDktNGNkMDFhYmIzM2Q0In0.oNg8ZOcUyLsrMbtSrA_fATA3pr4h-m7DB9GsMVU_FiCWJhqq6lC5sJFZNmQoNSfCMdmlNo_OmVTYO1oC14mgfx01LZuVRtgVticiT8frk5Ue953C_ec-urVW0UHdVIFvJU0XYedZU6TtOeW0L6iu6jmAOtTS78ndktkEzA434TNDEmy6_61TAs9dDmh7cARbkZeGRSvCPpYyws7jmD8f2Zvr34v5zz62sPrIGMUE1GTIPJYGVO8M9R7B-QM0IRUL0zuOQhbo2oaShNP8ApcRQbiUv1l8G2JB8jSJ8uSu_xAStfQessXd4MEMbmYof1koAz7UDbF7e6NWiWTuiRvbIQ" 

def user_create(role,email,firstName,lastName,middleName, countryCode,countryAlphaCode,dialNumber):
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

    headers = {"Activerole":"2", "Authorization":auth_token}
    response = requests.post(url, headers = headers ,json=payload)
    assert response.status_code == 200, response.text  
    json_data = response.json()
    print("UserCreatedSuccessfully.by Code." , json.dumps(json_data, indent=4))
    print(payload,"=====================")

user_create(2,"Raj02@mathur.com","Raj","Kumar","Mathur","+91","IN",64664646)