import csv
with open("Contenido\Ejemplosbasicos\covid.csv") as archi:
    import csv
    lector = csv.DictReader(archi)
    for fila in lector:
        print(fila["iso_code"], fila["continent"])

