# pip install -U pandasql

import pandas as pd
import pandasql as psql

data = pd.read_csv("Contenido\Ejemplosbasicos\owid-covid-data.csv",header=0)
pais=input("Ingrese país: ")
anio=input("Ingrese año (4 dig): ")
mes=input("Ingrese mes (2 dig): ")
resu=psql.sqldf("Select strftime('%m', date) as mes, sum(new_cases) as total from data where location='{}' and strftime('%Y', date)='{}' GROUP BY strftime('%m', date)".format(pais, anio))
print(resu)
