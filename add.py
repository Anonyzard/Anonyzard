#!/bin/env python3
# Script para agregar paquetes a la nueva lista
import json
import sys
salida = str(sys.argv[1])
with open(salida,"r") as archivo:
    datos = json.load(archivo)

name = input("\nEscribe el nombre del programa: ")
package = input("\nEscribe la URL de descarga del paquete: ")
version = input("\nIngresa la versión del programa: ")
icon = input("\nEscribe la URL del icono: ")
size = input ("\nEscribe el tamaño del programa (MiB): ")
description = input("\nEscribe una corta descripción del programa: ")
web = input("\nEscribe la URL de la web del programa: ")
mantainer = input("\nEscribe el nombre del mantenedor del paquete: ")
license = input("\nEscribe el nombre de la licencia del programa: ")
nuevo = {
        "name": name,
        "package": package,
        "version": version,
        "icon": icon,
        "size": size,
        "description": description,
        "web": web,
        "mantainer": mantainer,
        "license": license,
        "remote": True
    }
# datos["lpkg"].append = nuevo
# json.dump(datos, archivo_nuevo, indent=4, ensure_ascii=False)
#print(datos["lpkg"])
archivo.close()
# data = dict(datos)
# data["lpkg"].append = nuevo
with open(salida, 'w') as archivo_nuevo:
    datos["lpkg"].append(nuevo)
    datos["lpkg"] = sorted(datos["lpkg"], key=lambda x: x["name"])
    #print(datos)
    json.dump(datos, archivo_nuevo, indent=4, ensure_ascii=False)
archivo_nuevo.close()
