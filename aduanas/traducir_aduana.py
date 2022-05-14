import requests
import scrapy
import copy

urls = [
    # NOTE: aca hay que llenar las URLS que interesan. Estan en el d ocumento que se difundio
    # Para que funcione, usar http://aduanet.gob.pe   el https de ww3 sunat parece estar protegido o algo
    # Se puede usar los archivadores tambien
]


acc = []
for url in urls:
    partida = {}
    r = requests.get(url, verify=False)
    selector = scrapy.Selector(text=i['html'])

    f = lambda title, index: selector.xpath("//td/font[contains(text(), '{}')]/../following-sibling::td[{}]/font/text()".format(title, index)).extract_first()
    get_data = [
        "DECLARACION",
        "FECHA NUMERACION",
        "SUJETO A",

        "DECLARANTE",
        "IMPORTADOR",
        ("IMPORTADOR", 2),
        "MANIFIESTO",
        'FEC.LLEGADA',

        'TERMINAL',
        "5.5. TOTAL PESO NETO",
        "5.6. TOTAL PESO BRUTO",
        "5.7. TOTAL CANTIDAD BULTOS",
        "5.8. TOTAL UNIDADES FISICAS",
        "5.9. UNIDADES COMERCIALES",
        "TOTAL SERIES",
        "5.13 TIPO TRATAMIENTO",
        ('FOB', 2),
        ('FLETE', 2),
        ('SEGURO', 2),
        ('6.5. CIF', 2),
        "AD/VALOREM",
        "DERECHO ESPECIFICO",
        "IMP. SELECTIVO CONSUMO",
        "IMP. PROMOCION MUNICIPAL",
        "GENERAL A LA VENTA",
        "DERECHO ANTIDUMPING",
        "TASA SERVICIO DESPACHO",
        "ULTIMO DIA DE PAGO",
        "FECHA CANCELACION",
    ]
    for spec in get_data:
        index = 1
        if isinstance(spec, tuple): spec, index = spec
        partida[spec] = f(spec, index)
    
    partida['transporte_empresa'] = selector.xpath("//td/font[contains(text(), '{}')]/text()".format("4.3. EMPRESA")).extract_first()

    # Parseo de items
    total_rows = selector.xpath('//font[text() = "DESCRIPCION DE MERCANCIAS"]/../../following-sibling::tr')
    partida['n_items'] =  int(len(total_rows)/12)
    
    if partida['n_items'] > 10:
        continue

    if 'SPIKEVAX' in i['html']:
        dosis_index = -2
        lote_index = -3
        tipo = "MODERNA"

    elif 'COMIRNATY' in i['html']:
        dosis_index = -1
        lote_index = -3
        tipo = "PFIZER"
        if "0.1 COMIRNATY" in i['html']:
            partida['vacuna_subtipo'] = "pediatrica"

    elif 'VERO CELL' in i['html'].upper():
        dosis_index = -1
        lote_index = -2
        tipo = "SINOPHARM"

    elif 'ASTRAZENECA' in i['html'] or 'AZD1222' in i['html']:
        dosis_index = -2
        lote_index = -3
        tipo = "ASTRAZENECA"
        partida['vacuna_subtipo'] = 'azd1222' if 'AZD1222' in i['html'] else 'chadox'
    else:
        print("no se pudo clasificar", url)
        continue
    
    partida['vacuna'] = tipo

    c = lambda row_index, cell_index: rows[row_index].xpath(f'string(td[{cell_index}])').extract_first()
    for index in range(partida['n_items']):
        i = copy.deepcopy(partida)

        rows = total_rows[index*12:(index+1)*12]

        i['item_embarque_puerto'] = c(1, 2)
        i['item_embarque_guia_aerea'] = c(1, 3)
        i['item_embarque_fecha'] = c(1, 4)

        i['item_cantidad_bultos'] = c(2, 2)
        i['item_clase_bultos'] = c(2, 3)
        i['item_unidades_fisicas'] = c(2, 4)
        i['item_peso_neto'] = c(2, 5)
        i['item_peso_bruto'] = c(2, 6)
        i['item_moneda_transaccion'] = c(2, 7)
        i['item_fob_dolares'] = c(2, 8)
        
        i['item_flete'] = c(3, 2)
        i['item_seguro'] = c(3, 3)
        i['item_advalorem'] = c(3, 4)
        i['item_igv'] = c(3, 5)
        i['item_ipm'] = c(3, 6)
        i['item_isc'] = c(3, 7)

        i['item_pais_origen'] = c(4, 2)
        i['item_pais_adquisicion'] = c(4, 3)

        i['item_nandina'] = c(6, 2)
        i['item_nandina_descr'] = c(6, 3)

        for rindex in range(7, 12):
            i[f'descr_{rindex-6}'] = rows[rindex].xpath('string()').extract_first().strip()
        
        dosis = rows[dosis_index].xpath("string()").extract_first().strip()
        lote = rows[lote_index].xpath("string()").extract_first().strip()

        if tipo == "PFIZER":
            try:
                s = dosis.split("CON")
                if len(s) > 1:
                    i['n_dosis'] = s[-1].replace("DOSIS", "").strip()
            except:
                pass
        
        elif tipo == "SINOPHARM":
            try:
                i['n_dosis'] = dosis.rsplit("=")[-1].split("DOSIS")[0].split("TEMP")[0].strip(": ")
            except:
                pass

        elif tipo == "ASTRAZENECA":
            try:
                i['n_dosis'] = (dosis.split("TOTAL")[-1] if 'TOTAL' in dosis else dosis.split("=")[-1]).replace("DOSIS", "").strip(": ")
            except:
                pass
        
        elif tipo == "MODERNA":
            try:
                i['n_dosis'] = (dosis.split("TOTAL")[-1] if 'TOTAL' in dosis else dosis.split("=")[-1]).replace("DOSIS", "").strip(": ")
            except:
                pass

        acc.append(i)


import pandas as pd
df = pd.DataFrame(acc).drop_duplicates()
print(len(set(df['url'])), " duas para toda vacuna ", len(df), "items")
print(df.vacuna.value_counts())

df = df.sort_values(['vacuna'])
df.to_csv("vacunas.csv", index=False)
