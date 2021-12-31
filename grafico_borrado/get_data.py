import requests
import datetime
import traceback

today = datetime.date.today().strftime("%Y_%m_%d")

try:
# no se si la URL cambia...
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


# TODO: enviar al web archive esta URL cada dia
# https://archive.org/help/wayback_api.php