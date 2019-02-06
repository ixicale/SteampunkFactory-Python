#!/usr/bin/env python3.6

import random
import pyperclip
import json

'''
@author: Luis Fernando Reséndiz Gutiérrez

Script para generar y copiar en clipboard una petición aleatoria para realizar cargos en modo de pruebas.
Dependencias para instalar:
- pyperclip
'''

HOTEL = [
	'ZHSP',
	'ZMGR',
	'ZMNI',
	'ZMSU',
	'ZHBP',
	'ZHIM',
	'ZHLB',
	'ZRPL',
	'ZRCZ',
	'ZCJG',
	'ZPLB'
]
CIA = [
	'HPR',
	'OPR',
	'HER'
]
LIMIT_ITEMID = 80
LIMIT_CONCEPTOID = 10

REQUEST = {
  "idfin_cliente_interno": "1",
  "url_actualizacion" : "http://dev.api_url.local/",
  "reserva": "11002766",
  "usuario_creacion": "clever_online",
  "cargo":
  [
    {
      "cia": random.choice(CIA),
      "hotel": random.choice(HOTEL),
      "pago_detalle": ""
    }
  ]
}

def getItems():
	items = []
	for i in range(1, LIMIT_ITEMID):
		item = {
	            "id_item" : i,
	            "importe": "%.6f" % random.uniform(0.000001, 0.009999),
	            "idconcepto_ingreso": random.randint(1, LIMIT_CONCEPTOID),
	            "detalle_cargo" : "Test cargo"
        	}
		items.append(item)
	return items

def copyRequestToClipboard():
	REQUEST['cargo'][0]['pago_detalle'] = getItems()
	pyperclip.copy(json.dumps(REQUEST))
	spam = pyperclip.paste()

if __name__ == "__main__":
	copyRequestToClipboard()
