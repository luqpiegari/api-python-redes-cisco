"""Exporta a CSV el inventario IPv4 descubierto por Packet Tracer."""

import argparse
import csv
from getpass import getpass
import json
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def consultar(base, ruta, *, datos=None, ticket=None):
    headers = {"Accept": "application/json"}
    if ticket:
        headers["X-Auth-Token"] = ticket
    cuerpo = None
    if datos is not None:
        cuerpo = json.dumps(datos).encode("utf-8")
        headers["Content-Type"] = "application/json"
    solicitud = Request(f"{base}{ruta}", data=cuerpo, headers=headers)
    with urlopen(solicitud, timeout=15) as respuesta:
        return json.load(respuesta)["response"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("usuario", help="Usuario del Network Controller")
    parser.add_argument("--puerto", type=int, default=58000)
    parser.add_argument("--salida", type=Path, default=Path("inventario.csv"))
    args = parser.parse_args()
    base = f"http://localhost:{args.puerto}/api/v1"
    clave = getpass("Contraseña del controlador: ")

    try:
        sesion = consultar(base, "/ticket", datos={"username": args.usuario, "password": clave})
        ticket = sesion["serviceTicket"]
        equipos = consultar(base, "/network-device", ticket=ticket)
        hosts = consultar(base, "/host", ticket=ticket)
        if not isinstance(equipos, list) or not isinstance(hosts, list):
            raise ValueError("El controlador no devolvió listas de inventario.")

        with args.salida.open("x", encoding="utf-8-sig", newline="") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["categoria", "nombre", "ipv4", "modelo_o_tipo", "interfaz"])
            for equipo in equipos:
                writer.writerow([
                    "equipo", equipo.get("hostname"), equipo.get("managementIpAddress"),
                    equipo.get("platformId") or equipo.get("type"), "",
                ])
            for host in hosts:
                writer.writerow([
                    "host", host.get("hostName"), host.get("hostIp"),
                    host.get("hostType"), host.get("connectedInterfaceName"),
                ])
    except HTTPError as error:
        parser.exit(1, f"El controlador devolvió HTTP {error.code}.\n")
    except (URLError, OSError, ValueError, KeyError) as error:
        parser.exit(1, f"No se pudo exportar el inventario: {error}\n")

    print(f"Exportados {len(equipos)} equipos y {len(hosts)} hosts a {args.salida}")


if __name__ == "__main__":
    main()
