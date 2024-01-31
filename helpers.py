import requests
import json


def get_data(group_id, date):
    url = "http://127.0.0.1:8000/attendanse/"
    data = {"group_id": group_id, "attendance_day": date}
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    return response.json()
