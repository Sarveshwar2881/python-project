import requests, json
from URL import headers, base_url


def framework_add(Name,description,regulatoryBody,reg_url):
    url = base_url +"/framework/add"
    payload={                   
    "name": Name,
    "description": description,
    "regulatoryBody": regulatoryBody,
    "url": reg_url
}
    
    response = requests.post(url, headers = headers ,json=payload)
    assert response.status_code == 200, response.text  
    json_data = response.json()
    print("Framework added Successfully.by Code." , json.dumps(json_data, indent=4))
    F_id=json_data.get("id")
    return F_id



# # update Framework.
def framework_update(F_id, name, description, regulatoryBody, website):
    url = base_url +"/framework/update"
    payload={                   
    "id": F_id,
    "name": name,
    "description": description,
    "regulatoryBody": regulatoryBody,
    "url": website
}
    

    response = requests.post(url, headers = headers ,json=payload)
    assert response.status_code == 200, response.text  
    json_data = response.json()
    print("Framework update Successfully.by Code." , json.dumps(json_data, indent=4))
    print(F_id)



# # Framework Search by name

def framework_search(name):
   
    url = base_url +"/framework/list"
   
    payload={                   
        "id": "",
        "skip": 0,
        "limit": 0,
        "searchQuery": name
    }
    
    response = requests.post(url, headers = headers ,json=payload)
    response_json = response.json()
   
    if response_json.get("frameworkCount") == 0:
        print("framework not found")
    elif response.status_code == 200:    
        print("framework found successfully.", json.dumps(response_json, indent=4))
    else:
        print("Found error in framework.", response_json)



# F_id = framework_add("Name1002", "Description001 By Code", "By Code001","www.accorp01webportal.web.app")

# framework_update(F_id,"NewName1002", "Description001 By Code", "By Code001","www.accorp01webportal.web.app")

# framework_search("NewName1002")



