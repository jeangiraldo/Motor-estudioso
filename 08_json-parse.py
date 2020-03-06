# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

#Replace
import urllib.parse
import requests

main_api="https://www.mapquestapi.com/directions/v2/route?"
orig="Quito"
dest="Cuenca"
key="YGkKflOYOPm1PwEm59RukFin2aX5iuqI"

url=main_api+urllib.parse.urlencode({"key":key,"from":orig,"to":dest})

json_data=requests.get(url).json()
print(json_data)
