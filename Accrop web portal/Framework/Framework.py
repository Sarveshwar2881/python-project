import requests  
import json  

base_url="https://70mzbzwmea.execute-api.ap-south-1.amazonaws.com" 

auth_token="Bearer eyJraWQiOiJlYlZZOTl5XC8yK0ZoY0NHOFNyMFk2NSsrUWFwYitwWkxicksyWjNzOXFuWT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI0MTczOGRiYS02MGMxLTcwMWItYTA0OS00Y2QwMWFiYjMzZDQiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtc291dGgtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aC0xX2duSkJqWHFEQiIsImNsaWVudF9pZCI6IjRmaHQ5cjUwZnFrdGdxZjZxc2VraXRmYWlnIiwib3JpZ2luX2p0aSI6ImZkNGQ0YzE4LTVmZjQtNGJlOC04NTRjLWFmOTc2ZWM3NTFmMyIsImV2ZW50X2lkIjoiNWYzZjVlMTItYzZhOC00ZDE3LTg0MjAtZjg3MzcwNDA3N2IyIiwidG9rZW5fdXNlIjoiYWNjZXNzIiwic2NvcGUiOiJhd3MuY29nbml0by5zaWduaW4udXNlci5hZG1pbiIsImF1dGhfdGltZSI6MTc1MDA2NTY3NiwiZXhwIjoxNzUwMTUyMjE5LCJpYXQiOjE3NTAwNjU4MTksImp0aSI6IjMxYzQxYzQ0LWI5ODQtNDk2OC1iNTliLWYxOGNmY2MxZGMxYiIsInVzZXJuYW1lIjoiNDE3MzhkYmEtNjBjMS03MDFiLWEwNDktNGNkMDFhYmIzM2Q0In0.KgPBvWJHYXAwihknoatscH88TCp6Hv_Pz1V4wNZSRvJ7IocAleRZXbZAiUgfUf-XQaYI16S7esMzpU16kpBqxpiiPMHARPnX7TofZnWeT1Z23LiNQqnwU5wa8b1kdkXW2F6OdEXip-m0KY89ZZ1mh__KySNqi9YcG9TsuNI0gkFhYl6uHv3A0DgXTyE5eMk6sj2VWUFgxAZguEGDvIwcPaFjE6KkVp2GNEeu48mamWtDaLLlP9XuFLm2P4yjtMJbhWypkU3sFtUF3DIF3U7KMeD-p8KLieGTm1B4EshtSBwgd9DfdHwXrFf86cWV74W19cfK7B5bxvQoASbZLJ_Aow"

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
def framework_search(name):
    url = base_url +"/framework/list"
          
    if name is framework_search:
        print("Framework found")
    else: 
        print("framework not found")
        
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
framework_update("684bf3b5af606a2b0ec68eba","ByCodeFrame003", "Description003 By Code", "By Code003","www.flipkart.com")
#framework_search("ByCodeFrame003")