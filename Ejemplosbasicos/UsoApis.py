import requests
import json
nombre=input("Ingrese el nombre deseado: ")
conversionSexo={"male":"masculino", "female":"femenino"}

url="https://api.agify.io"
argum={"name": nombre}
resp=requests.get(url, params=argum)
if resp.status_code==200:
    # print(resp.text)
    dict=resp.json()
    edad=dict["age"]

url="https://api.genderize.io"
resp=requests.get(url, params=argum)
if resp.status_code==200:
    # print(resp.text)
    dict=resp.json()
    sexo=conversionSexo[dict["gender"]]
    probabilidad=dict["probability"]

url="https://api.nationalize.io"
resp=requests.get(url, params=argum)
if resp.status_code==200:
    # print(resp.text)
    dict=resp.json()
    codpais=dict["country"][0]["country_id"]
    probabPais=round(dict["country"][0]["probability"],2)

# Así obtengo el país
url="https://restcountries.eu/rest/v2/alpha/"+codpais
resp=requests.get(url)
if resp.status_code==200:
    # print(resp.text)
    dict=resp.json()
    pais=dict["name"]


print("{} es un nombre {} con una probabilidad de {}. La edad promedio de las personas con ese nombre es de {}. Y hay una probabilidad de {} de que sea de {}"
    .format(nombre, sexo, probabilidad, edad, probabPais, pais))


