#Módulos que se usarán
import requests #Para entender solicitudes
import json #Para reconocer el formato json
from getpass import getpass
import os
from tabulate import * #Para crear tablas

baseUri = "http://localhost:58000/api/v1" #URL de PT

# Llamada al API por el ticket
headers = {"Content-Type": "application/json"} #Headers
usuario = os.getenv("PT_NC_USER") or input("Usuario del controlador: ")
clave = os.getenv("PT_NC_PASSWORD") or getpass("Contraseña del controlador: ")
data = json.dumps({"username": usuario, "password": clave})
resp = requests.post(baseUri+"/ticket", data=data, headers=headers) #URL específica

print("Status de Solicitud:")
print(resp.status_code)
resp.raise_for_status()
result = resp.json()
# print(result)

ticket = result["response"]["serviceTicket"] #Printing ticket


# Llamada al API para recibir los dispositivos de red
headers = {"X-Auth-Token": ticket}
resp = requests.get(baseUri+"/network-device", headers=headers) #URL específica
resp.raise_for_status()

# print (resp.status_code)
result = resp.json()
#print (json.dumps(result, indent=4))
print("\nDispositivos de Red:")
host_list=[]
i=0
for item in result["response"]:
    i+=1
    host_list.append([i,item.get("hostname") or "(sin nombre)",item.get("serialNumber") or "-",item.get("softwareVersion") or "-"])
    #print(item["hostname"]+" "+item["serialNumber"]+" "+item["softwareVersion"]) #Lista completa

print(tabulate(host_list,headers=["Nº","Hostname","Serial Number","Software Version"],tablefmt='rst')) #Tabla ordenada 

# Llamada al API para recibir los host
headers = {"X-Auth-Token": ticket }
resp = requests.get(baseUri+"/host", headers=headers) #URL específica
resp.raise_for_status()

# print (resp.status_code)
result = resp.json()
#print (json.dumps(result, indent=4))
print("\nHosts de la Red:")
host_list=[]
i=0
for item in result["response"]:
    i+=1
    host_list.append([i,item.get("hostName","-"),item.get("hostType","-"),item.get("hostIp","-")])
    #print(item["hostName"]+" "+item["hostType"]+" "+item["hostIp"]) #Lista completa

print(tabulate(host_list,headers=["Nº","Hostname","Tipo","IP"],tablefmt='rst')) #Tabla ordenada 
