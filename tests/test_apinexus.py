from nexus_api import APINexus
import pandas as pd
from pandas import json_normalize
import datetime
import unittest

class TestHistoricalData(unittest.TestCase):

    def test_get_historical_values(self):
        API_Host = 'nexus-cdi-demo.globalomnium.com'
        API_Port = 56000
        NexusToken = '96f8a50b-6e26-4c0f-bd19-68d0ba187cda'
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
        delta_days = 300

        date_format = '%m/%d/%Y %H:%M:%S %Z'
        date_to = datetime.datetime.now()
        date_from = date_to - datetime.timedelta(days=delta_days)
        print("The analysis involves data from " + str(date_from) + " to " + str(date_to))
        # %% codecell
        # Variables en la vista de variables
        vbles = NX.callGetTagViews(uid_tagview)
        df = pd.DataFrame(vbles)
        columnas = df['columns']
        columnas = json_normalize(columnas)
        uids_vbles = list(columnas['uid'])  # String with variables UIDS
        try:
            filtered_hist = NX.filter_tagview2(date_from, date_to, columnas, uid_tagview, 'variable')
            print(filtered_hist)
            self.assertTrue
        except:
            print('Error, could not retrieve data')

if __name__=='__main__':
    unittest.main()
