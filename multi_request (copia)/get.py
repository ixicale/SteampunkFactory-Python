import requests
import os
import json
from datetime import datetime, timedelta
import time
import threading


def get_file_content(fname):
    fname = os.path.abspath(os.path.dirname(__file__)) + "/" + fname
    exists = os.path.isfile(fname)
    if not exists:
        print(not_found_msg.format(fname=fname))
        sys.exit(1)
    with open(fname) as file:
        return file.read()


REQUESTS = get_file_content("data/list.json")
SQL_LIST = json.loads(REQUESTS)["data"]
BASE = "https://s3.amazonaws.com/webfiles_palace/clever/products/assets"
TEMPLATE_INS = """
INSERT INTO `clv_products`.`service_servicio_asset` (`idservice_servicio`, `idcliente`, `path`, `externo`, `thumb`, `estado`, `usuario_creacion`, `fecha_creacion`, `usuario_ultima_modificacion`, `fecha_ultima_modificacion`) VALUES ({id_servicio}, '1', '{path_img}', '1', '{path_img_tumb}', '1', 'ixicale', '2020-06-04 00:00:00', 'ixicale', '2020-06-04 00:00:00');
"""


def contar(path, **item):
    """Contar hasta cien"""

    response = requests.get(url=path)
    # response = requests.get(
    #     "http://s3.amazonaws.com/webfiles_palace/clever/products/assets/agatha_blush.jpg"
    # )
    if response.status_code == 200:
        query = TEMPLATE_INS.format(**item)
        with open("./resp.txt", "a") as out:
            out.write(query + "\n")


    # pastebin_url = r.text
    # resp = json.loads(pastebin_url)


def run(parameter_list):
    for item in parameter_list:
        index = parameter_list.index(item)
        _service = ((item["service"]).lower()).replace(" ", "_")
        _codigo_produccion = ((item["codigo_produccion"]).lower()).replace(
            " ", "_"
        )
        for name in [_service, _codigo_produccion]:
            for exten in ["png", "PNG", "JPG", "jpg"]:
                path = "{base}/{name}.{exten}".format(
                    name=name, exten="png", base=BASE
                )
                path2 = "{base}/{name}_thumb.{exten}".format(
                    name=name, exten="png", base=BASE
                )
                try:
                    # hilo1 = threading.Thread(target=contar)
                    hilo1 = threading.Thread(
                        target=contar,
                        args=(path,),
                        kwargs={
                            **item,
                            "path_img": path,
                            "path_img_tumb": path2,
                        },
                    )
                    hilo1.start()
                    if index % 5 == 0:
                        time.sleep(1.45)
                except Exception:
                    time.sleep(0.45)
                    t = threading.Thread(target=write_request, args=(path))
                    t.start()


run(SQL_LIST)
