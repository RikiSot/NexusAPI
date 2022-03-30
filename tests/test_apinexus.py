import datetime
import os
import time
from pathlib import Path
from unittest import TestCase

import numpy as np
import pandas as pd
from dotenv import load_dotenv, find_dotenv
from pandas import json_normalize

from src.nexus_api import APINexus

# Set test options and .env file
desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 10)

BASE_DIR = Path('..')
dotenv_path = BASE_DIR / 'secrets.env'
load_dotenv(find_dotenv(dotenv_path))

API_HOST = os.getenv("API_HOST")
ALARM_ID = os.getenv('ALARM_ID')
NEXUS_TOKEN = os.getenv('NEXUS_TOKEN')

class TestAPINexus(TestCase):
    API_Host = API_HOST
    API_Port = 56000
    NexusToken = NEXUS_TOKEN
    version = 'v1'
    # New object pointing to HOST and Port selected with Nexus Token
    NX = APINexus.APINexus(API_Host, API_Port, NexusToken, version)

    def test_status_connection(self):
        response = self.NX.statusConnection(self.NX.url_NX)
        self.assertEqual(response, 200)

    def test_filter_installation(self):
        # Leer variables asociadas al token
        datos = self.NX.callGetTags()
        columnas = json_normalize(datos)

        # Profundidad del análisis en fechas desde hoy
        delta_days = 3
        date_to = datetime.datetime.now()
        date_from = date_to - datetime.timedelta(days=delta_days)
        try:
            filtered_hist = self.NX.filter_installation(date_from, date_to, columnas, '', resolucion=4)
            print(filtered_hist)
            self.assertTrue(1)
        except Exception as e:
            print(e)
            self.fail()

    def test_filter_tagview(self):
        # Leer vistas de variables asociadas al token
        tagviews = self.NX.callGetDocuments()
        tagviews = json_normalize(tagviews)
        # Busqueda del uid de la vista que contiene los niveles
        uid_tagview = tagviews.uid[0]

        # Profundidad del análisis en fechas desde hoy
        delta_days = 3

        date_to = datetime.datetime.now()
        date_from = date_to - datetime.timedelta(days=delta_days)
        print("The analysis involves data from " + str(date_from) + " to " + str(date_to))

        # Variables en la vista de variables
        vbles = self.NX.callGetTagViews(uid_tagview)
        df = pd.DataFrame(vbles)
        columnas = df['columns']
        columnas = json_normalize(columnas)
        try:
            filtered_hist = self.NX.filter_tagview(date_from, date_to, columnas, uid_tagview, '')
            print(filtered_hist)
            self.assertTrue(1)
        except Exception as e:
            print(e, 'Error, could not retrieve data')
            self.fail()

    def test_get_alarms_uids_by_names(self):
        uids = self.NX.get_alarms_uids_by_names('Low Input Flow')
        print(uids)
        self.assertEqual(uids[0], ALARM_ID)

    def test_get_alarms_uids_by_groups(self):
        uids = self.NX.get_alarms_uids_by_groups('Low Level')
        print(uids)
        self.assertEqual(uids[0], ALARM_ID)

    def test_call_get_alarm_byuid(self):
        uid = self.NX.get_alarms_uids_by_groups('Low Level')[0]
        print(self.NX.callGetAlarmByuid(uid))
        self.assertTrue(1)

    def test_call_post_ack_alarm(self):
        try:
            self.NX.callPostAckAlarm(ALARM_ID)
            self.assertTrue(1)
        except Exception as e:
            print(e)
            self.fail()

    def test_call_post_tag_insert(self):
        try:
            self.NX.callPostTagInsert('api_test')
            self.assertTrue(1)
        except Exception as e:
            print(e)
            self.fail()

    def test_call_post_value_rtmult_epoch(self):
        try:
            test_df = pd.DataFrame({'timeStamp': [time.time()], 'name': ['api_test'], 'value': [1]})
            self.NX.callPostValueRTmult(test_df)
            self.assertTrue(1)
        except Exception as e:
            print(e)
            self.fail()

    def test_call_post_hist_value_epoch(self):
        try:
            test_df = pd.DataFrame({'timeStamp': [time.time()], 'name': ['api_test'], 'value': [1]})
            self.NX.callPostValueHist(test_df)
            self.assertTrue(1)
        except Exception as e:
            print(e)
            self.fail()

    def test_call_post_hist_value_datetime(self):
        try:
            now = datetime.datetime.now()
            print(now, type(now)) # print(now)
            test_df = pd.DataFrame({'timeStamp': [now], 'name': ['api_test'], 'value': [1]})
            self.NX.callPostValueHist(test_df)
            self.assertTrue(1)
        except Exception as e:
            print(e)
            self.fail()

    def test_call_post_ack_alarm(self):
        try:
            response = self.NX.callPostAckAlarm(ALARM_ID, 'ARE')
            content = response.text
            print(content)
            if 'Alarm is not in a status that can be acknowledged' in content:
                self.assertTrue(1)
            else:
                self.assertEqual(response.status_code, 200)
        except Exception as e:
            print(e)
            self.fail()

    def test_call_post_alarm_event(self):
        try:
            response = self.NX.callPostAlarmEvent(ALARM_ID, 'test')
            self.assertEqual(response.status_code, 200)
        except Exception as e:
            print(e)
            self.fail()

