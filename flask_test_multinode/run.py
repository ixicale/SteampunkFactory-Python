# importa la variable que tenga todas las rutas asignadas
from lib.dispatcher import app

# ejecuta el programa con flask del objeto dispatcher.py
app.run(port=2323, debug=True)
