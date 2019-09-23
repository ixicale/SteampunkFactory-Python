"""
Script para generar un archivo CSV
que permita el analisis de los multiples POST
"""

import os
import sys
import csv
import json
from datetime import datetime, timedelta
import threading
import time
import requests


not_found_msg = """
File Not Found ({FNAME}).
Check the file and restart again
"""
csv.register_dialect(
        'myDialect',
        delimiter='\t',
        quotechar='"',
        quoting=csv.QUOTE_ALL,
        skipinitialspace=True)


def get_file_content(fname):
    fname = os.path.abspath(os.path.dirname(__file__)) + "/" + fname
    exists = os.path.isfile(fname)
    if not exists:
        print(not_found_msg.format(fname=fname))
        sys.exit(1)
    with open(fname) as file:
        return file.read()


REQUESTS = get_file_content("requests.txt").splitlines()
PROPE = get_file_content("properties.txt").splitlines()
NOW = datetime.now()
FNAME = os.path.abspath(os.path.dirname(__file__)) \
    + "/resp/" + NOW.strftime("%Y%m%d_%H%M%S_rates.csv")
QA = "http://rates-api-qa.clever.palace-resorts.local"
API_ENDPOINT = QA + "/rateview/levels"
TITLES = [
    "NO_PAYLOAD",
    "PAYLOAD",
    "FB_REQUEST",
    "FE_REQUEST",
    "F_INICIO_RESPONSE",
    "F_FIN_RESPONSE",
    "PROP",
    "TARIFA",
    "NIVEL",
    "JSON_NIVELES",
    "NUM_ITEM",
    "NUM_tARIFA",
    "NUM_NIVEL",
    "AMOUNT",
    "MAX_POR_NVL",
    "MIN_POR_NVL",
    "Error",
    "response error",

]


def writeCSV():
    print("creating: ", FNAME)
    with open(FNAME, 'w') as csvFile:
        writer = csv.writer(csvFile, dialect='myDialect')
        writer.writerow(TITLES)
    csvFile.close()


def appendCSV(row):
    # print(row)

    with open(FNAME, 'a') as csvFile:
        writer = csv.writer(csvFile, dialect='myDialect')
        writer.writerow(row)
    csvFile.close()


def subProcess(propiedad, index, data):
    val = json.loads(data)
    semana = 7 * index
    date_format = "%Y-%m-%d"

    dateTrvlBeginStr = val["travelBegin"]
    dateTrvlBeginObj = datetime.strptime(dateTrvlBeginStr, date_format)
    val["travelBegin"] = dateTrvlBeginObj + timedelta(days=semana)
    val["travelBegin"] = val["travelBegin"].strftime(date_format)

    dateTrvlEndStr = val["travelEnd"]
    dateTrvlEndObj = datetime.strptime(dateTrvlEndStr, date_format)
    val["travelEnd"] = dateTrvlEndObj + timedelta(days=semana)
    val["travelEnd"] = val["travelEnd"].strftime(date_format)

    val["resort"] = propiedad

    data = json.dumps(val)
    r = requests.post(url=API_ENDPOINT, data=data)
    print(data)
    pastebin_url = r.text
    resp = json.loads(pastebin_url)

    NO_PAYLOAD = index
    PAYLOAD = data
    F_INICIO = ""
    F_INICIO = ""
    F_FIN = ""
    PROP = ""
    TARIFA = ""
    Amount = ""
    NIVEL = ""
    JSON_NIVELES = ""
    try:
        if not resp["error"] & (type(resp["data"]) is not None):

            # print(resp, pastebin_url, end="\n__________________\n", sep="\n")
            
                
            dataList = resp["data"]
            data_p = 0
            for data in dataList:
                data_p = data_p + 1
                ListTarifa = data["items"]
                TARIFA = len(ListTarifa) > 0
                F_INICIO = data["travel_begin"]
                F_FIN = data["travel_end"]
                PROP = data["resort"]

                if TARIFA:
                    tarifa_p = 0
                    for tarif in ListTarifa:
                        tarifa_p = tarifa_p + 1
                        JSON_NIVELES = tarif["levels"]
                        NIVEL = len(JSON_NIVELES) > 0
                        Amount = tarif["amount"]

                        if NIVEL:
                            lvl_p = 0
                            for lvl in JSON_NIVELES:
                                lvl_p = lvl_p + 1
                                appendCSV([
                                    NO_PAYLOAD,
                                    PAYLOAD,
                                    val["travelBegin"],
                                    val["travelEnd"],
                                    F_INICIO,
                                    F_FIN,
                                    PROP,
                                    TARIFA,
                                    NIVEL,
                                    JSON_NIVELES,
                                    data_p,
                                    tarifa_p,
                                    lvl_p,
                                    Amount,
                                    lvl["max"],
                                    lvl["min"]
                                ])
                        else:
                            appendCSV([
                                NO_PAYLOAD,
                                PAYLOAD,
                                val["travelBegin"],
                                val["travelEnd"],
                                F_INICIO,
                                F_FIN,
                                PROP,
                                TARIFA,
                                NIVEL,
                                JSON_NIVELES,
                                data_p,
                                tarifa_p,
                                "",
                                Amount,
                                "",
                                ""
                            ])
                else:
                    appendCSV([
                        NO_PAYLOAD,
                        PAYLOAD,
                        val["travelBegin"],
                        val["travelEnd"],
                        F_INICIO,
                        F_FIN,
                        PROP,
                        TARIFA,
                        False,
                        "",
                        data_p,
                        "",
                        "",
                        "",
                        "",
                        ""
                    ])
        else:
            appendCSV([
                NO_PAYLOAD,
                PAYLOAD,
                val["travelBegin"],
                val["travelEnd"],
                "",
                "",
                propiedad,
                False,
                False,
                "",
                "",
                "",
                "",
                "",
                lvl["max"],
                lvl["min"]
            ])
    except Exception as e:
        appendCSV([
            NO_PAYLOAD,
            PAYLOAD,
            val["travelBegin"],
            val["travelEnd"],
            "",
            "",
            "",
            False,
            False,
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            str(e),
            r.text
        ])


def requester():
    writeCSV()
    for propiedad in PROPE:
        k = 0
        for data in REQUESTS:
            k = k + 1
            for index in range(0, 53):
                print(k, propiedad, index)
                t = threading.Thread(target=subProcess, args=(propiedad, index, data,))
                t.start()
                if index%10 == 0:
                    time.sleep(0.75)


requester()
