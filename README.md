# Entorno de virtualización Python

# Pasos de instalación en Linux:

## 1. Clonación del proyecto

Desde la terminal ejecutar:

**git clone** <URL_del_repositorio> <nombre_de_la_carpeta_de_destino>

Luego ejecutar **cd** <nombre_de_la_carpeta_de_destino>. Esta carpeta será la raíz de nuestro proyecto en Python.

## 2. Creación del entorno virtual

Supongamos que el nombre que le damos al entorno virtual es **cisco**, entonces se creará una carpeta **cisco** con todas las librerías y dependencias necesarias paea nuestro proyecto. 

La manera de realizarlo es la siguiente:

# python3 -m venv <nombre_del_entorno>
Ejemplo: python3 -m venv cisco

Para activar el entorno escribimos **source cisco/bin/activate**, en la carpeta raíz del proyecto. El nombre del entorno virtual aparecerá entre paréntesis ().

## 3. Instalación de las dependencias, en este caso las librerías requests y tabulate

En la carpeta raíz de nuestro proyecto y dentro del entorno virtual escribimos: **pip install -r requirements.txt**

## 4. Selección del intérprete Python para nuestro entorno virtual

<img width="881" height="118" alt="image" src="https://github.com/user-attachments/assets/18c41d8e-d338-48b6-953c-b2499c57319f" />

<img width="736" height="412" alt="image" src="https://github.com/user-attachments/assets/2a795fcd-2cf8-47ef-a5a6-d21e09ce967f" />

Tal como se ve en la figura seleccionamos Python 3.10.12 (cisco) que se mostrará como entorno recomendado.

## 5. Desactivación del entorno virtual

Simplemente escribimos en la línea de comandos: **deactivate**



## Antes de ejecutar los scripts

Habilitá el acceso externo del controlador en Packet Tracer y dejá el puerto `58000`. Ejecutá los scripts desde la raíz del repositorio.

| Script | Función |
| --- | --- |
| `python src/01_get-ticket.py` | Pide el usuario y la contraseña y obtiene un ticket temporal. |
| `python src/02_get-network-device.py` | Pide el ticket y consulta los equipos de red, incluido el ISP descubierto sin credenciales. |
| `python src/03_get-host.py` | Pide el ticket y consulta los hosts y sus interfaces. |
| `python src/04_tabulate.py` | Obtiene su propio ticket y muestra ambos inventarios como tablas. |
| `python src/inventario_csv.py USUARIO --salida inventario.csv` | Obtiene su propio ticket y exporta equipos y hosts a un CSV nuevo. |

Los scripts de la cátedra también admiten las variables locales `PT_NC_USER`, `PT_NC_PASSWORD` y `PT_NC_TICKET`, según el script. El ticket vence y permite acceder a la API mientras está vigente. Conservá los tickets y contraseñas fuera del repositorio público.
