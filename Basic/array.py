
import pandas as pd
import numpy as np
import requests


# zx = []
# print(len(zx))
# if(len(zx) is not 0):
#     print("no es 0")
# else:
#     print("es 0")


# a = {}
# print (a)
# a['index'] = ["sol","luna","estella"]
# b = a['index']
# print (a)
# a['value'] = b
# print (a)



r={
  "report_title": "Reporte de Ventas por Planner",
  "values": [
    "Total",
    "Service Amount"
  ],
  "index": [
    "idclv_propiedad",
    "a"
  ],
  "attributes": [
    # "Block Code-a",
    # "Event-a",
    # "Event Name-a",
    # "Paid Amount-a",
    # "Pending Balance-a",
    # "Resort-a",
    # "Service Amount-a",
    # "Total Amount-a",
    # "Wedding's Date-a",
    #
    # "idclv_propiedad-b",
    # "Income_Amount-b",
    # "Pendin_balanse-b",
    # "Service Amount-b",
    # "services-b",
    # "Total_sales-b",
    # "user-b",
    #
    # "idclv_propiedad-c",
    # "Income Amount-c",
    # "Pending balanse-c",
    # "Total-c",
    # "Service Amount-c"
    "Block Code",
    "Event",
    "Event Name",
    "Paid Amount",
    "Pending Balance",
    "Resort",
    "Service Amount",
    "Total Amount",
    "Wedding's Date",

    "idclv_propiedad",
    "Income_Amount",
    "Pendin_balanse",
    "Service Amount",
    "services",
    "Total_sales",
    "user",

    "idclv_propiedad",
    "Income Amount",
    "Pending balanse",
    "Total",
    "Service Amount"
  ],
  "endpoint": [
    "events/statistics/detailservicepayment/mvicente",
    "events/statistics/balansepaymentservices/mvicente/",
    "events/statistics/salesbyuser/mvicente"
  ],
  "row": 50
}




if __name__ == '__main__':

    endpoint = r['endpoint']
    index = r['index']
    values = r['values']
    report_title = r['report_title']


    'Definir titulos y definir indices del diccionario'
    columns = r['attributes']
    json_title =[]
    dict_json = {}
    cont=0
    rtn = []
    for col in columns:
        if not col in json_title:
            # print("se agrego a la lista")
            json_title.append(col)
            dict_json[col] = []

    # rtn.append(json_title)
    # rtn.append(dict_json)

    # Variables para trabajar las las api
    url_proxy = "http://core-api-qa.clever.palace-resorts.local/report/interface/"
    # Bucle por api
    for ep in endpoint:
        # Ruta de la api a leer y la invoca
        url_report = url_proxy + ep
        r = requests.get(url_report)
        # Retorna el Json de la api
        json_request = r.json()
        # print(str(json_request) + "\n\n")
        error = json_request["error"]
        cont+=1
        if not error:
            data = json_request["data"]
            print(str(cont) +"°:\n" + str(data) + "\n\n")
            # Filtro por nombre dentro de la columna data de la api
            for col in json_title:
                for d in data:
                    # Agregar toda la informacion a un diccionario general (unir todos las apis)
                    if col in d.keys():
                        dict_json[col].append(d[col])
                    else:
                        dict_json[col].append(None)

                # print(str(col) + "tiene longitud de: " + str(len(dict_json[col]))) # Controlar la cantidad de datos recibidos

        else:
            print("response 204, Not Data Requested")
