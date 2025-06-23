import requests , json 
from URL import headers, base_url
from Framework import F_id


def add_criteria(code, description, F_id):
    url = base_url +"/criteria/add"
    payload={                   
    "code": code,
    "description": description,
    "frameworkId": F_id
}
    response = requests.post(url, headers= headers, json=payload)
    assert response.status_code == 200, response.text  
    json_data = response.json()
    print("Criteria added Successfully.by Code." , json.dumps(json_data, indent=4))
    CID=json_data.get("id")
    print(CID)
    return CID 

add_criteria("Frame Code 004","Description by Code",F_id)

#--------------------------------------------------------------------------------------

# Edit Criteria
# def update_criteria(cid, code, description, Fid):
#     url = base_url +"/criteria/update"
#     payload={                   
#     "id": cid,
#     "code": code,
#     "description": description,
#     "frameworkId": Fid
# }
#     response = requests.post(url, headers= headers, json=payload)
#     assert response.status_code == 200, response.text  
#     json_data = response.json()
#     print("Criteria added Successfully.by Code." , json.dumps(json_data, indent=4))
   

# update_criteria(cid,"ByCode001","Description by Code",id)