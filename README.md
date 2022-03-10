# NexusAPI
Este repositorio tiene como propósito reunir en una única libería todas las funciones necesarias para trabajar con la API de Nexus en Python.
En lugar de importar los archivos a la carpeta del proyecto cada vez que se usan puede instalarse la librería en la PATH de Python 



## Instalación

Usa el package manager pip para instalar la librería. Por el momento, no está publicada en ningún repositorio online así que hay que instalar el archivo de forma manual especificando la ruta del archivo .whl. Si se abre la consola desde la carpeta del proyecto:

    > pip install dist/nexus_api-0.1.0-py3-none-any.whl

## Uso
Para importar todo el contenido de la librería, una vez instalada hay que realizar el siguiente import:

    import nexus_api
Si únicamente se desea la clase en la que residen las funciones que trabajan con la API:

    from nexus_api import APINexus
Lo que otorga acceso a la clase ClaseNexus en la que residen todas las funciones necesarias.

### Ejemplo de uso
Un ejemplo de uso para la famosa función GetFiltered que permite filtrar el histórico de variables entre un periodo dado:

En primer lugar se especifican los parámetros de conexión y se crea el objeto Nexus, además de los imports necesarios
```
from nexus_api import APINexus
import pandas as pd
import datetime
```

    API_Host = 'nexus-cdi-demo.globalomnium.com'  
    API_Port = 56000 
    NexusToken = '96f8a50b-6e26-4c0f-bd19-68d0ba187cda' 
    version = 'v1'
    NX = APINexus.APINexus(API_Host, API_Port, NexusToken, version)
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

## Contribuir

Cualquier función o sugerencia añadida es bien recibida.

Sugerencias:

-   Falta documentar las funciones de la API
-   Sería conveniente contar con un gestor de paquetes interno para poder instalar el paquete desde un repositorio de Nexus

## Contacto
[**Pau Juan**](mailto:pau.juan@nexusintegra.io)
*Operaciones*


[**Laura Moreno**](mailto:laura.moreno@nexusintegra.io)
*Operaciones*


[**Ricardo Gómez**](mailto:ricardo.gomez.aldaravi@nexusintegra.io)
*Operaciones*

[Nexus Integra](https://nexusintegra.io/)