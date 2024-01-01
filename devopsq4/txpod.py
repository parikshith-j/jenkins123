import requests
import json
import time

# Define the JSON data to send
json_data = {
    "key1": "value1",
    "key2": "value2"
}

# Use the Kubernetes service name (flask-service) to reach the Flask application
url = "http://commrecv:5000/receive_json"

headers = {
    'Content-Type': 'application/json'
}

# Send POST request with JSON data
while (True):

    response = requests.post(url, headers=headers, data=json.dumps(json_data))

    if response.status_code == 200:
        print("JSON message sent successfully")
    else:
        print("Failed to send JSON message")
    time.sleep(5)
