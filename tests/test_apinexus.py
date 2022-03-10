from nexus_api import APINexus
from nexus_api import NexusRequest as NR
import pandas as pd
from pandas import json_normalize
import datetime
import unittest


class TestHistoricalData(unittest.TestCase):


    def get_historical_values_tagview(self):
        API_Host = 'nexus-cdi-demo.globalomnium.com'
        API_Port = 56000
        NexusToken = 'xxxxxxx'
        version = 'v1'
        # New object pointing to HOST and Port selected with Nexus Token
        NX = APINexus.Clase_Nexus(API_Host, API_Port, NexusToken, version)

        # Leer vistas de variables asociadas al token
        tagviews = NX.callGetDocuments()
        tagviews = json_normalize(tagviews)
        # Busqueda del uid de la vista que contiene los niveles
        uid_tagview = tagviews.uid[0]

        # # 1. Traer datos de entrenamiento de la API

        # Profundidad del análisis en fechas desde hoy
        delta_days = 3

        date_format = '%m/%d/%Y %H:%M:%S %Z'
        date_to = datetime.datetime.now()
        date_from = date_to - datetime.timedelta(days=delta_days)
        print("The analysis involves data from " + str(date_from) + " to " + str(date_to))

        # Variables en la vista de variables
        vbles = NX.callGetTagViews(uid_tagview)
        df = pd.DataFrame(vbles)
        columnas = df['columns']
        columnas = json_normalize(columnas)
        uids_vbles = list(columnas['uid'])  # String with variables UIDS
        try:
            filtered_hist = NX.filter_tagview(date_from, date_to, columnas, uid_tagview, 'var')
            print(filtered_hist)
            print('Prueba para escribir un 1 en la variable WTP_pumped_current_month: ')
            #print(NX.callPostValueRT('WTP_pumped_current_month', float(1)))
            self.assertTrue
        except:
            print('Error, could not retrieve data')


    def test_get_from_installation(self):
        # Parametros Inyección instancia Nexus
        API_Host = 'nexus-pyland.uksouth.cloudapp.azure.com'
        API_Port = 56000
        NexusToken = 'xxxxxxx'
        version = 'v1'
        # New object pointing to HOST and Port selected with Nexus Token
        NX = APINexus.Clase_Nexus(API_Host, API_Port, NexusToken, version)

        # Leer variables asociadas al token
        datos = NX.callGetTags()
        columnas = json_normalize(datos)

        # Profundidad del análisis en fechas desde hoy
        delta_days = 3

        date_format = '%m/%d/%Y %H:%M:%S %Z'
        date_to = datetime.datetime.now()
        date_from = date_to - datetime.timedelta(days=delta_days)
        #print("The analysis involves data from " + str(date_from) + " to " + str(date_to))

        #try:
        filtered_hist = NX.filter_installation(date_from, date_to, columnas, 'a', resolucion=4)
        print (filtered_hist)
        #print('Prueba para escribir un 1 en la variable WTP_pumped_current_month: ')
        #print(NX.callPostValueRT('WTP_pumped_current_month', float(1)))
        self.assertTrue
        # except:
        #     print('Error, could not retrieve data')


if __name__=='__main__':
    unittest.main()
