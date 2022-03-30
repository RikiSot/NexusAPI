# nexus_integra_api
Este repositorio tiene como propósito reunir en una única libería todas las funciones necesarias para trabajar con la API de Nexus en Python.
En lugar de importar los archivos a la carpeta del proyecto cada vez que se usan puede instalarse la librería en la PATH de Python 

## Table of Contents

* [Instalación](#chapter1)
* [Uso](#chapter2)
* [Ejemplos](#chapter3)
* [Contrubuir](#chapter4)
* [Change Log](#chapter5)
* [Contacto](#chapter6)

## Instalación <a class="anchor" id="chapter1"></a>

Usa el package manager pip para instalar la librería. Puede instalarse de forma local o desde el repositorio de PyPi

```
pip install nexus_integra_api
```

## Uso <a class="anchor" id="chapter2"></a>
Para importar todo el contenido de la librería, una vez instalada hay que realizar el siguiente import:

    import nexus_api
Si únicamente se desea la clase en la que residen las funciones que trabajan con la API:

    from nexus_api import APINexus
Lo que otorga acceso a la clase APINexus en la que residen todas las funciones necesarias.

## Ejemplo de uso <a class="anchor" id="chapter3"></a>
Un ejemplo de uso para la famosa función GetFiltered que permite filtrar el histórico de variables entre un periodo dado:

En primer lugar se especifican los parámetros de conexión y se crea el objeto Nexus, además de los imports necesarios
```
from nexus_api import APINexus
import pandas as pd
import datetime

API_Host = 'nexus-cdi-demo.globalomnium.com'  
API_Port = 56000 
NexusToken = 'xxxxxxxxxxxxxxxxx' 
version = 'v1'
NX = APINexus.APINexus(API_Host, API_Port, NexusToken, version)
```
Después es necesario obtener el uid de la vista de variables que se quiere leer (también existe función para leer desde instalación)
```
# Leer vistas de variables asociadas al token  
tagviews = NX.callGetDocuments()  
tagviews = json_normalize(tagviews)  
# Busqueda del uid de la vista
uid_tagview = tagviews.uid[0]
```
Se especifica la ventana temporal deseada:
```
# Profundidad del análisis en fechas desde hoy  
delta_days = xxx  
date_format = '%m/%d/%Y %H:%M:%S %Z'  
date_to = datetime.datetime.now()  
date_from = date_to - datetime.timedelta(days=delta_days)
```
Hay que especificar las variables deseadas de la vista de variables elegida. Con este código se obtienen todos los uids de las variables de la vista. Es necesario filtrar 
```
# Variables en la vista de variables  
vbles = NX.callGetTagViews(uid_tagview)  
df = pd.DataFrame(vbles)  
columnas = df['columns']  
columnas = json_normalize(columnas)  
uids_vbles = list(columnas['uid'])  # String with variables UIDS
```
Finalmente se obtiene el histórico llamando a la función:
```
filtered_hist = NX.filter_tagview(date_from, date_to, columnas, uid_tagview, 'variable')
```


## Contribuir <a class="anchor" id="chapter4"></a>

Cualquier función o sugerencia añadida es bien recibida.

Sugerencias:

- Falta documentar las funciones de la API
- Traducir documentación

## Change log <a class="anchor" id="chapter5"></a>

v0.4.0 - 30/03/2022

**Added**
  
- API V2 alarm functions
  * callPostAckAlarm(uid, status)
  * callPostAlarmEvent(uid, msg)
  * callGetAlarms()
  * callGetAlarmByuid(uid)
  * get_alarms_uids_by_names([names])
  * get_alarms_uids_by_groups([groups])
- Unit tests
- .env file in order protect credentials
- Bypassed 50k row limit in POST methods
- Added support to datetime objects in callPostValueHist
  
**Modified**
  
- Unified callPostValueHist and callPostValueHistmult (deprecated)
  
###v0.3.2 - 11/03/2022
**Added**
- Add filter_installation and filter_tagview as replacement for GetFiltered
- Add README.md

## Contacto <a class="anchor" id="chapter6"></a>
[**Pau Juan**](mailto:pau.juan@nexusintegra.io)
*Operaciones*


[**Laura Moreno**](mailto:laura.moreno@nexusintegra.io)
*Operaciones*


[**Ricardo Gómez**](mailto:ricardo.gomez.aldaravi@nexusintegra.io)
*Operaciones*

[Nexus Integra](https://nexusintegra.io/)