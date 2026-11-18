from getpass import getpass
import os
import requests
api_url = "http://localhost:58000/api/v1/host"

headers = {"X-Auth-Token": os.getenv("PT_NC_TICKET") or getpass("Ticket del controlador: ")}

resp = requests.get(api_url, headers=headers)

print("Request status: ", resp.status_code)
resp.raise_for_status()

response_json = resp.json()
print (response_json)
print()
print()
hosts = response_json["response"]

for host in hosts:
    print(host.get("hostName", "-"), "\t", host.get("hostIp", "-"), "\t", host.get("hostMac", "-"), "\t", host.get("connectedInterfaceName", "-"))
