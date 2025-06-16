import requests  
import json  

base_url="https://70mzbzwmea.execute-api.ap-south-1.amazonaws.com" 

auth_token="Bearer eyJraWQiOiJlYlZZOTl5XC8yK0ZoY0NHOFNyMFk2NSsrUWFwYitwWkxicksyWjNzOXFuWT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI0MTczOGRiYS02MGMxLTcwMWItYTA0OS00Y2QwMWFiYjMzZDQiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtc291dGgtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aC0xX2duSkJqWHFEQiIsImNsaWVudF9pZCI6IjRmaHQ5cjUwZnFrdGdxZjZxc2VraXRmYWlnIiwib3JpZ2luX2p0aSI6ImZhNWUzN2RiLTIwZGEtNGZmNi1iYTM0LTVhYzg4NDdmYzQ4YiIsImV2ZW50X2lkIjoiYWZkNGIyMjctNzliNi00ZWMzLThmMGItNDc5ZDYxMTY0NzRlIiwidG9rZW5fdXNlIjoiYWNjZXNzIiwic2NvcGUiOiJhd3MuY29nbml0by5zaWduaW4udXNlci5hZG1pbiIsImF1dGhfdGltZSI6MTc0OTgwMzQ4MiwiZXhwIjoxNzQ5ODkzMDQ2LCJpYXQiOjE3NDk4MDY2NDYsImp0aSI6ImYzM2ExN2E5LTNiNTItNDk0Ni1hNmEyLWE4ZWE3NDBlODBhYSIsInVzZXJuYW1lIjoiNDE3MzhkYmEtNjBjMS03MDFiLWEwNDktNGNkMDFhYmIzM2Q0In0.Xs4eW7CEcfegEzfiA68izSKe9Z-yQphPfjhEN1zJ0MIWU6nI12ePXvlNeYOnOVlL5k5wQUQwUD-6A00Rm3jQxJiRLj77fd5dmT_WTZur6Wenj6kkc8dVgAcQX0_9vCw7ktuvIHxMMaQJPwB0Emi9nnKlIpKyidDV76tNbobeN8D4IwJuuwbcpqmtjOO-Tabldpc9SNt9y4UDLUZX-BZ79DEmrVvqrcyGRU3s3FzbVfX1ghXhWVGWXoNNw3cz0kF3e-Wgh47QIhixKkWvhmcyv7MYkD1MXy-cIMWRnLqe9K4Dphjp6I_PqL0tmDF-zhJPECPSwfI-5XSG7q93TxKm0Q"

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
    Fwork_id=json_data.get("id")
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
def framework_search(searchquery):
    url = base_url +"/framework/list"
    payload={                   
    "id": "",
    "skip": 0,
    "limit": 0,
    "searchQuery": searchquery
}
    headers = {"Activerole":"2", "Authorization":auth_token}
    response = requests.post(url, headers = headers ,json=payload)
    assert response.status_code == 200 
    json_data = response.json()
    print("Framework search Successfully.by Code." , json.dumps(json_data, indent=4))

   




id = framework_add("ByCodeFrame003", "Description003 By Code", "By Code003","www.accorpwebportal.web.app")
framework_update(id,"ByCodeFrame003", "Description003 By Code", "By Code003","www.flipkart.com")
framework_search("ByCodeFrame003")