import json
from getpass import getpass
import os
import requests
api_url = "http://localhost:58000/api/v1/ticket"

headers = {
    "content-type": "application/json"
}

body_json = {
    "username": os.getenv("PT_NC_USER") or input("Usuario del controlador: "),
    "password": os.getenv("PT_NC_PASSWORD") or getpass("Contraseña del controlador: ")
}

resp = requests.post(api_url, json.dumps(body_json), headers=headers)

print("Ticket request status: ", resp.status_code)
response_json = resp.json()
resp.raise_for_status()
serviceTicket = response_json["response"]["serviceTicket"]

print("The service ticket number is: ", serviceTicket) 
