import requests  
import json  

base_url="https://70mzbzwmea.execute-api.ap-south-1.amazonaws.com" 

auth_token="Bearer eyJraWQiOiJlYlZZOTl5XC8yK0ZoY0NHOFNyMFk2NSsrUWFwYitwWkxicksyWjNzOXFuWT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI0MTczOGRiYS02MGMxLTcwMWItYTA0OS00Y2QwMWFiYjMzZDQiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtc291dGgtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aC0xX2duSkJqWHFEQiIsImNsaWVudF9pZCI6IjRmaHQ5cjUwZnFrdGdxZjZxc2VraXRmYWlnIiwib3JpZ2luX2p0aSI6IjhhMzExOTgxLWQ5MjQtNDE0NC1iOTc4LTE1MmM2YjVmZjQwNSIsImV2ZW50X2lkIjoiNDljN2Y3ZmItN2E5ZC00M2Q3LTg4YWYtZmExMGY2OTkwZTdiIiwidG9rZW5fdXNlIjoiYWNjZXNzIiwic2NvcGUiOiJhd3MuY29nbml0by5zaWduaW4udXNlci5hZG1pbiIsImF1dGhfdGltZSI6MTc0OTcwODYxNiwiZXhwIjoxNzQ5ODA0Mjg3LCJpYXQiOjE3NDk3MTc4ODcsImp0aSI6ImIwNWU1MGEyLWVmYjAtNDAwMi04NDAyLTdhODBlZDU3N2ViMCIsInVzZXJuYW1lIjoiNDE3MzhkYmEtNjBjMS03MDFiLWEwNDktNGNkMDFhYmIzM2Q0In0.oNg8ZOcUyLsrMbtSrA_fATA3pr4h-m7DB9GsMVU_FiCWJhqq6lC5sJFZNmQoNSfCMdmlNo_OmVTYO1oC14mgfx01LZuVRtgVticiT8frk5Ue953C_ec-urVW0UHdVIFvJU0XYedZU6TtOeW0L6iu6jmAOtTS78ndktkEzA434TNDEmy6_61TAs9dDmh7cARbkZeGRSvCPpYyws7jmD8f2Zvr34v5zz62sPrIGMUE1GTIPJYGVO8M9R7B-QM0IRUL0zuOQhbo2oaShNP8ApcRQbiUv1l8G2JB8jSJ8uSu_xAStfQessXd4MEMbmYof1koAz7UDbF7e6NWiWTuiRvbIQ" 

def framework_add(Name,description,regulatoryBody,url):
    url = base_url +"/framework/add"

    payload={                   
    "name": Name,
    "description": description,
    "regulatoryBody": regulatoryBody,
    "url": url
}

    headers = {"Activerole":"2", "Authorization":auth_token}
    response = requests.post(url, headers = headers ,json=payload)
    assert response.status_code == 200, response.text  
    json_data = response.json()
    print("Framework added Successfully.by Code." , json.dumps(json_data, indent=4))
    
    Fworkid=json_data.get("id")
    print(Fworkid)
    return Fworkid

framework_add("ByCodeFrame002", "Description002 By Code", "By Code002","https://accorpwebportal.web.app/frameworkmanagement")


# update Framework.
def framework_update(fwordid,name,description,regulatoryBody,url):
    url = base_url +"/framework/update"

    payload={                   
  
    "id": fwordid,
    "name": name,
    "description": description,
    "regulatoryBody": regulatoryBody,
    "url": url
}

    headers = {"Activerole":"2", "Authorization":auth_token}
    response = requests.post(url, headers = headers ,json=payload)
    assert response.status_code == 200, response.text  
    json_data = response.json()
    print("Framework added Successfully.by Code." , json.dumps(json_data, indent=4))
  

framework_update("ByCodeFrame002", "Description002 By Code", "By Code002","https://accorpwebportal.web.app/frameworkmanagement")

#Get by id search framework.