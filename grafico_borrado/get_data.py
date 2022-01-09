import requests
import datetime
import traceback

today = datetime.date.today().strftime("%Y_%m_%d")

try:
    # TODO no se si la URL cambia..., probar y automatizar
    r = requests.get("https://cloud.minsa.gob.pe/s/8EsmTzyiqmaySxk/download", headers={'User-Agent': ':V'})
except:
    print("Error en request inicial", traceback.format_exc())

if r.status_code == 200:
    filename = r.headers['Content-Disposition'].split("=")[-1].strip('"')
    if 'csv' in filename:
        fmode, fattr = 'w', 'text'
        print(today, "# de lineas", len(r.text.split("\n")))

    else:
        fmode, fattr = 'wb', 'content'

    with open(f"{today}_{filename}", fmode) as F:
        F.write(getattr(r, fattr))

else:
    print(today, "status code != 200", r.headers)



# Archivando
requests.get("https://web.archive.org/save/https://cloud.minsa.gob.pe/s/8EsmTzyiqmaySxk/download")


# TODO, chequear mas las posiblidades de archivamiento
# https://archive.org/help/wayback_api.php


# Check availability
# https://archive.org/wayback/available?url=https://cloud.minsa.gob.pe/s/8EsmTzyiqmaySxk/download
# Response example
# {"url": "https://cloud.minsa.gob.pe/s/8EsmTzyiqmaySxk/download", "archived_snapshots": {"closest": {"status": "200", "available": true, "url": "http://web.archive.org/web/20211231193400/https://cloud.minsa.gob.pe/s/8EsmTzyiqmaySxk/download", "timestamp": "20211231193400"}}}


# 107642 2021_12_31_TB_FALLECIDO_HOSP_VAC.csv

# 2021_12_31 # de lineas 107642
# 2022_01_04 # de lineas 107825
# 2022_01_06 # de lineas 107770
# 2022_01_08 # de lineas 107836