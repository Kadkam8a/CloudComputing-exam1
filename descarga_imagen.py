

import requests
import shutil
import time


# funcion que descarga una imagen del sol desde internet
def descarga_imagen(i):
    url = "https://sdo.gsfc.nasa.gov/assets/img/latest/latest_1024_HMIIC.jpg" 
    r = requests.get(url, stream=True)  # usando el metodo GET de la libreria requests. GET es un VERBO de HTTP
    if r.status_code == 200:  # si la respuesta del servidor es 200 OK, continuamos
        with open('latest_{}.jpg'.format(i), 'wb') as f:  # abrimos un archivo para escritura 
            r.raw.decode_content = True  # decodificamos los bytes
            shutil.copyfileobj(r.raw, f) # escribimos la imagen en el archivo abierto

lines = []
with open('update_time.conf', 'r') as fconf:  # leemos el archivo conf
    lines = fconf.readlines()  # readlines detecta los saltos de linea (denotado por el caracter '\n') y coloca todas las lineas en una lista
deltas = [int(x.strip('\n')) for x in lines]  # los datos vienen como "strings", hay que pasarlos al tipo entero (int())



for i, dt in enumerate(deltas): # por cada dato de configuracion en el archivo conf
    descarga_imagen(i)  # llamamos la funcion de arriba 
    time.sleep(dt*60)   # mandamos a dormir al programa) por el numero de minutos especificado, time.sleep toma segundos, por lo que multiplicamos por 60



# EOF   


