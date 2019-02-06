#!/usr/bin/env python3.6
import json
import requests
import time

import pandas as pd
import numpy as np


# Definir el punto de recuperación de datos
url_proxy = "http://core-api-qa.clever.palace-resorts.local/report/interface/"
end_point= "events/statistics/balansepaymentservices/mvicente/"

print(url_proxy  + end_point)
# Conexión con la api y obtención del JSON
response = requests.get(url_proxy  + end_point)

# print (response)
# Escribir JSON
data = json.loads(response.content)
error = (data['error'])

if not error:

    # arr= data['atributos']
    ar2 = ['idclv_propiedad', 'Service Amount', 'Total']

    r = response

    rdata = r.json()
    rdata = rdata["data"]
    a =  np.asarray(rdata)
    df = pd.DataFrame(rdata)

    # print(arr['bar'])

    data_kind = []
    dict_json = {}

    for tipo in ar2:# bucle con datos por caracteristica del hijo
        data_kind = []
        for item in rdata:#iterar datos por hijo del json
            # print (item)
            data_kind.append(item[tipo])
        dict_json[tipo]= data_kind
    # print(dict_json)

    values = []
    for tipo in ar2:# bucle con datos por caracteristica del hijo
        # print("\n" + tipo + ": ")
        # print(dict_json[tipo])

        # Agregar el arreglo para la tabla cross
        values.append(np.array(dict_json[tipo], dtype=object))

    print("\n\n\n")

    # print (values)
    print(pd.crosstab(values[0], [values[1], values[2]],
                rownames=[ar2[0]], colnames=[ar2[1], ar2[2]]))


else:
    print("Error de conexión, verifica tu enlace de conexión.")
