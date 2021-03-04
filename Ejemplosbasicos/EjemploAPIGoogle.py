# -*- coding: utf-8 -*-

# Sample Python code for youtube.videos.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
from typing import List, Any, Union

import googleapiclient.discovery
import googleapiclient.errors
import json

scopes = ["https://www.googleapis.com/auth/youtube",
          "https://www.googleapis.com/auth/youtube.force-ssl",
          "https://www.googleapis.com/auth/youtube.readonly",
          "https://www.googleapis.com/auth/youtubepartner"]

def main():
    archivo = open("datos.csv", "w")
    api_service_name = "youtube"
    api_version = "v3"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey="ACA DEBERIAN PONER LA KEY CORRESPONDIENTE QUE GENERAN CUANDO HABILITAN EL SERVICIO EN GOOGLE")
    ids = ['hRQUgi0xCm8', 'Itqr8xnGirk', 'M5dCZaj72Mk', 'UmGQno0m7IA', 'BqDgzSAEN1Q', 'LBMEuNxXr30', 'CbGbkUdzeKc',
           'CNxbbRKwRPY', 'GMQW26hAHKE', 'TJ0VIfTcfLE', '6Q2_n00BW4E', 'w7nj3VvXxyg', 'gG3wGtWEdYs', 'Vv35blRXro4',
           'DkLt8m1gFU4', 'M6V8szWVAYs', 'QQql9JOQZss']
    idsBB = ['Xo18wv3SAuM', 'Xu-hx84AA8c', 'Pavp-_4WcQs', 'bAm2jNuuvWU', 'reaj3Y8mbXI', 'AsXjec5U6LA']
    num=1
    for video in ids:
        request = youtube.videos().list(
            part="statistics",
            id=video
        )
        response = request.execute()
        cantidad=response['items'][0]['statistics']['viewCount']
        comentarios=response['items'][0]['statistics']['commentCount']
        salida=str(num)+ ";"+cantidad+ ";"+ comentarios+ '\n'
        print(salida)
        archivo.write(salida)
        num+=1
    num=1
    for video in idsBB:
        request = youtube.videos().list(
            part="statistics",
            id=video
        )
        response = request.execute()
        cantidad=response['items'][0]['statistics']['viewCount']
        comentarios=response['items'][0]['statistics']['commentCount']
        salida="B&B"+str(num)+ ";"+cantidad+ ";"+ comentarios+ '\n'
        print(salida)
        archivo.write(salida)
        num+=1

    archivo.close()
if __name__ == "__main__":
    main()