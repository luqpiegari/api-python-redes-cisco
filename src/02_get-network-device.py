from getpass import getpass
import os
import requests
api_url = "http://localhost:58000/api/v1/network-device"

headers = {"X-Auth-Token": os.getenv("PT_NC_TICKET") or getpass("Ticket del controlador: ")}

resp = requests.get(api_url, headers=headers)

print("Request status: ", resp.status_code)
resp.raise_for_status()

response_json = resp.json()
print()
print()
print (response_json)
print()
print()
networkDevices = response_json["response"]

for networkDevice in networkDevices:
    print(networkDevice.get("hostname") or "(sin nombre)", "\t", networkDevice.get("platformId") or "-", "\t", networkDevice.get("managementIpAddress") or "-")
