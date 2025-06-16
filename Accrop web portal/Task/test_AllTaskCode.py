import requests
import json  
import csv

base_url = "https://70mzbzwmea.execute-api.ap-south-1.amazonaws.com"
auth_token = "Bearer eyJraWQiOiJlYlZZOTl5XC8yK0ZoY0NHOFNyMFk2NSsrUWFwYitwWkxicksyWjNzOXFuWT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI0MTczOGRiYS02MGMxLTcwMWItYTA0OS00Y2QwMWFiYjMzZDQiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtc291dGgtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aC0xX2duSkJqWHFEQiIsImNsaWVudF9pZCI6IjRmaHQ5cjUwZnFrdGdxZjZxc2VraXRmYWlnIiwib3JpZ2luX2p0aSI6ImU3NTA2YzZkLTgxOTQtNGFmNC1iNzMxLTdjMDg3MWZkMGEyNiIsImV2ZW50X2lkIjoiZjkyNTMzMGYtNGNiMy00ZDRiLTgxMDQtOGFiMGMyZjgyYzcyIiwidG9rZW5fdXNlIjoiYWNjZXNzIiwic2NvcGUiOiJhd3MuY29nbml0by5zaWduaW4udXNlci5hZG1pbiIsImF1dGhfdGltZSI6MTc0OTE5MDQ1NywiZXhwIjoxNzQ5Mjc2ODgxLCJpYXQiOjE3NDkxOTA0ODEsImp0aSI6IjA1MjAxYTg1LWYyNTYtNDk5NS05MmYwLTQ4NGNhODAyM2Q0YyIsInVzZXJuYW1lIjoiNDE3MzhkYmEtNjBjMS03MDFiLWEwNDktNGNkMDFhYmIzM2Q0In0.BVTqop-TdG75MN6DBbd1SDqZ6f5vf9UYTQfjk8v_RZmov6KXTBzcXHA171w0RFKKAv8rHfU8f6IaW5D7ocG571hCMApqg9OQ4bTIhci2oR46glGpP6UgU2hL7oZCSJ9_388UJlPdsgkimYeHeJBacj4jXec8Gl0fK2bc5w6TsqCwib2Dh2__ue7aM_94puS3Ilcydpp9qv8DslfMH5eae-4q4jYAEUEG0s-3U7Hk2wA9zEvISJ5_U-x7SrpnFsW3YzMZMDmnc6xc4o3MZ8tZq-t6088CJOC-dQfdsLIgQ2GZdiEoI51Kg6MyHsqrWygzOdA2TiVWxQmFN6lRdwyuDw"

def test_task_create(name, des, code, feq):
    # Input validation
    if not name or not code:
        print(f"Skipped task creation: 'name' or 'code' is missing. name='{name}', code='{code}'")
        return

    url = base_url + "/testattribute/add"
    payload = {
        "name": name,
        "description": des,
        "frequency": feq,
        "code": code,
        "custom_days_default": 5
    }

    headers = {"Activerole": "2", "Authorization": auth_token}
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        json_data = response.json()
        print("Task Created Successfully:", json.dumps(json_data, indent=4))
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error for task '{name}': {http_err}")
    except Exception as err:
        print(f"Error for task '{name}': {err}")

# Run tasks
test_task_create("taskname006", "des006", "testcode006", 2)
test_task_create("taskname007", "", "testcode007", 3)  # This will still run
test_task_create("taskname008", "des008", "testcode008", 4)
test_task_create("", "des009", "", 5)  # This will be skipped due to missing name/code
test_task_create("taskname010", "des0010", "testcode010", 4)


# For crete a file.f

# f = open(r"C:\Users\Sarveshwar Kumar\Desktop\Sarvesh\python\python-project\Accrop Project\Task\task.xlsx", "w")
# f.write("Customer More Option\nEdit\nDisable\nManage Payment\nManage Framework\nManage Department\nManage People\nManage Control\nManage Task\nView Dashboard\nManage Audit")
# print(f)
# print(type(f))
# f.close()


# f = open(r"C:\Users\Sarveshwar Kumar\Desktop\Sarvesh\python\python-project\Accrop Project\Task\Task Result.xlsx", "rw")
# data = f.data
# f.write("Show Task Result")
# print(f)
# f.close()

