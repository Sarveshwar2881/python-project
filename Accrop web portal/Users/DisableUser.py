
import requests
import json  

base_url="https://70mzbzwmea.execute-api.ap-south-1.amazonaws.com"

auth_token="Bearer eyJraWQiOiJlYlZZOTl5XC8yK0ZoY0NHOFNyMFk2NSsrUWFwYitwWkxicksyWjNzOXFuWT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI0MTczOGRiYS02MGMxLTcwMWItYTA0OS00Y2QwMWFiYjMzZDQiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtc291dGgtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aC0xX2duSkJqWHFEQiIsImNsaWVudF9pZCI6IjRmaHQ5cjUwZnFrdGdxZjZxc2VraXRmYWlnIiwib3JpZ2luX2p0aSI6IjYyZjZkZTJiLWViMDMtNGNiYy1hZDI5LWVmMTRlNGNjZmM5OSIsImV2ZW50X2lkIjoiYTAyMTgwMmUtYTdhMi00OGQ4LWIwNWMtZjMwNGIwNzhlMTc5IiwidG9rZW5fdXNlIjoiYWNjZXNzIiwic2NvcGUiOiJhd3MuY29nbml0by5zaWduaW4udXNlci5hZG1pbiIsImF1dGhfdGltZSI6MTc0OTA5OTcyNSwiZXhwIjoxNzQ5MTg5NTIwLCJpYXQiOjE3NDkxMDMxMjAsImp0aSI6ImM1OTRiNWFhLWMwYjYtNGRiNS1iNTJjLWU4YmRkMTRhMzgzYiIsInVzZXJuYW1lIjoiNDE3MzhkYmEtNjBjMS03MDFiLWEwNDktNGNkMDFhYmIzM2Q0In0.Gu9L9LCrSOqDmsIJs4MM7t0twUKrXboFz-jgVHgXJ3x_vHQP3-kCAwdO4RNhox14mvlGLQVJC7sOD_agslyJIVXopYeHI7DGDmRAIk_C9HgVtXJnUdN5oqAO0ffUq99SSR8KmgLbcOhv5P_qEtGiu-X7BlH6DeWCZZTf-HDI7B2emL4YnJkShcURzsR19bf5cy6PJN6J-ZsabqhclGrN4LirHgtH_voAKxINLOoX6CFv6dHkvJtZGnFSmAVG4tys9wb7uRGN7ObzKgEu83uxMwI47_AsBLTCUJsub3XtYv0e9gIeCv4sEQG8bvRqcyPKf2sN-0Td00NBkkeE3asx7g"
def user_disable():
    url = base_url +"/user/disable"
    paylod={    
    "id": "68401eca5bae83f2c9bdf833",
    "remarks": "Diabaled by code."
}

    
    headers= {"Activerole":"2", "Authorization":auth_token}
    response = requests.post(url, headers = headers ,json=paylod)
    assert response.status_code == 200, response.text 
    json_data = response.json()
    print("Disabled this user by Code." , json.dumps(json_data, indent=4))

user_disable()

