# f= open ("Innocent.txt", "a")
# f.write("Any data(this data is write in file.)")
# f.close()


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


with open(r"C:\Users\Sarveshwar Kumar\Desktop\Sarvesh\python\python-project\Accrop web portal\Users\URL.py", "a+") as f:
    data = f.write("This is first line data.\n this is second line data.")  # <- add parentheses here
    print(data)
    print(type(data))





