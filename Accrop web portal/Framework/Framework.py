import requests  
import json 
from Users.URL import headers, base_url


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
    

    response = requests.post(targeturl, headers = headers ,json=payload)
    
    assert response.status_code == 200, response.text  
    json_data = response.json()
    print("Framework update Successfully.by Code." , json.dumps(json_data, indent=4))


# Get by id search framework.

def framework_search(name):
   
    url = base_url +"/framework/list"
   
    payload={                   
        "id": "",
        "skip": 0,
        "limit": 0,
        "searchQuery": name
    }
    
   
    response = requests.post(url, headers = headers ,json=payload)
    res_json = response.json()
   
    if res_json.get("frameworkCount") == 0:
        print("framework not found")
    elif response.status_code == 200:    
        print("framework found successfully.", json.dumps(res_json, indent=4))
    else:
        print("Found error in framework.", res_json.text)



#id = framework_add("ByCodeFrame001", "Description001 By Code", "By Code001","www.accorpwebportal.web.app")
framework_update("684bf3b5af606a2b0ec68eba","ByCodeFrame003", "Description003 By Code", "By Code003","www.flipkart.com")
framework_search("bycode")