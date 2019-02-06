'Detener procesos y ejecutar metodos asincronos'
import threading, time
'Leer, crear, eliminar ficheros'
import os
import shutil
'Convertir fechas y operaciones con fechas'
from datetime import datetime
from datetime import timedelta
'Texto a Hash'
import hashlib

def clean():
    filename = "Documents"
    dir = (os.listdir("."))
    if not filename in dir:
        # Crear nuevo fichero que no existe
        os.mkdir(filename)
    else:
        # Destruye el fichero con todos los archivos que contiene y crea uno limpio
        shutil.rmtree(filename)
        os.mkdir(filename)
    return(datetime.now() + timedelta(seconds=9))


def file_manager():
    date_file = datetime.now()
    kill_date = (datetime.now() + timedelta(seconds=9))
    clean()
    while 1:
        try: 
            dir = (os.listdir("."))
            date = datetime.now()
            if date >=  kill_date: # Si pasa una hora desde que inicio el proceso
                d = clean()
                if d is not None:
                    kill_date = d
                    print(kill_date)
        except Exception as e:
            print ("Error:", e)
        # Espera para comprobar cómo sube el consumo de CPU
        time.sleep(2) #3600

if __name__ == "__main__":
    
    print ("Inicio")
    
    threading.Thread(target=file_manager).start()
    print ("Fin")
    
    
    file = open("Documents/test.txt","w")
    
    file.write("lineas")
    file.close()
    

    
    
    