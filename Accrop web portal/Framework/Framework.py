import requests  
import json  

base_url="https://70mzbzwmea.execute-api.ap-south-1.amazonaws.com" 

auth_token="Bearer eyJraWQiOiJlYlZZOTl5XC8yK0ZoY0NHOFNyMFk2NSsrUWFwYitwWkxicksyWjNzOXFuWT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI0MTczOGRiYS02MGMxLTcwMWItYTA0OS00Y2QwMWFiYjMzZDQiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtc291dGgtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aC0xX2duSkJqWHFEQiIsImNsaWVudF9pZCI6IjRmaHQ5cjUwZnFrdGdxZjZxc2VraXRmYWlnIiwib3JpZ2luX2p0aSI6Ijk0M2YyYWE2LWFlNmUtNGU3MS1hNmFkLWMyNDliN2VkMTA0ZSIsImV2ZW50X2lkIjoiZTA1MzJkOGItYzQ5My00NjQwLTk4MDAtM2MwNWMzZmRmZTA0IiwidG9rZW5fdXNlIjoiYWNjZXNzIiwic2NvcGUiOiJhd3MuY29nbml0by5zaWduaW4udXNlci5hZG1pbiIsImF1dGhfdGltZSI6MTc1MDA2ODk3NywiZXhwIjoxNzUwMTU1Mzg0LCJpYXQiOjE3NTAwNjg5ODQsImp0aSI6ImUxNDRjZjM2LTVkOWYtNDdkNy1hMWM4LWZlOGI2MGRlNmIzZSIsInVzZXJuYW1lIjoiNDE3MzhkYmEtNjBjMS03MDFiLWEwNDktNGNkMDFhYmIzM2Q0In0.YfZ072Zg202OTWu87fRRn2ScfmIJrPUa6NZ43SGrrAeCIUnU0qBxLPNB5J1nlaiOseuB8k1qacyOJoBp1fLELdw06_27Q4uyMiI5wVPDjqru2vSFds0PLet2Twk7aJSqKMLBKCpmbDHKQanq3OZ7jwWIgSxIhWAy5zYnASF1JgaliRNEY6Q_rYbqj6KV6OgyfY2o7c2I4IlRxiaVMoBj_5F193QP9VlyGA4XamVWSibW0UE-MCh_9r1ytohygdo_DVIeUpGR1-5jf-F5eWM7A2BFtEM5W3JOpBGzNFs2mEY7O4Wm14X3T7SnLwXONE_eE4Wm7XRDBmkAv8DoJ5wWiw"

def framework_add(Name,description,regulatoryBody,reg_url):
    url = base_url +"/framework/add"
    payload={                   
    "name": Name,
    "description": description,
    "regulatoryBody": regulatoryBody,
    "url": reg_url
}
    headers = {"Activerole":"2", "Authorization":auth_token}
    response = requests.post(url, headers = headers ,json=payload)
    assert response.status_code == 200, response.text  
    json_data = response.json()
    print("Framework added Successfully.by Code." , json.dumps(json_data, indent=4))
    Fwork_id=json_data.get("name")
    print(Fwork_id)
    return Fwork_id



# update Framework.
def framework_update(Fwork_id,name,description,regulatoryBody,website):
    targeturl = base_url +"/framework/update"
    payload={                   
    "id": Fwork_id,
    "name": name,
    "description": description,
    "regulatoryBody": regulatoryBody,
    "url": website
}
    headers = {"Activerole":"2", "Authorization":auth_token}
    response = requests.post(targeturl, headers = headers ,json=payload)
    assert response.status_code == 200, response.text  
    json_data = response.json()
    print("Framework update Successfully.by Code." , json.dumps(json_data, indent=4))


# Get by id search framework.
def framework_search(frameworkCount):
    url = base_url +"/framework/list"
    if frameworkCount  == 0:
        print ("Framework not found.")    
           
    payload={                   
        "id": "",
        "skip": 0,
        "limit": 0,
        "searchQuery": name
    }
    headers = {"Activerole":"2", "Authorization":auth_token}
    response = requests.post(url, headers = headers ,json=payload)
    assert response.status_code == 200, response.text
    json_data = response.json()
    print("Framework search Successfully.by Code." , json.dumps(json_data, indent=4))






# id = framework_add("ByCodeFrame003", "Description003 By Code", "By Code003","www.accorpwebportal.web.app")
# framework_update("684bf3b5af606a2b0ec68eba","ByCodeFrame003", "Description003 By Code", "By Code003","www.flipkart.com")
framework_search("ByCodeFrame003")