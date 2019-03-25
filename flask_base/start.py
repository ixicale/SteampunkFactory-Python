#!/usr/bin/env python3.6
# importa la variable que tenga todas las rutas asignadas
from app.config import servicio


# ejecuta flask del objeto __init__
def main():
    servicio.run(port=2323, debug=True)


if __name__ == '__main__':
    main()
