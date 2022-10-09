from cmath import isnan
import pandas as pd
import os
import numpy as np


"""
función:        generarListaDict

parámetros:     rutaArchivo     str     Recibe como string la ruta donde se encuentra el archivo excel
                nombrePestaña   str     String que representa el nombre de la pestaña (en el excel) cuyos datos se quieren extraer, por ahora no se usa - se toma 1era pestaña

explicación:    Se convierte un archivo excel conteniendo los datos de alumnos y sus amigos/enemigos a DataFrame, y crea una lista con estos, 
                además de un diccionario que contiene "contadores de amistad" para cada uno (amigos son +1 y enemigos -1).

output:         listaAlu    list    Contiene todos los datos de cada alumno 
                dictAmigos  dict    Contiene contadores de amistad para cada alumno

nota:           Se asume que los nombres de las columnas en el excel serán: "id", "Nombre", 1, 2, 3, 4, 5, 6.

"""

def generarListaDict(rutaArchivo, nombrePestaña):
    listaAlu = []
    dictAmigos = dict()

    # Setear cwd en el directorio del archivo actual:
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    
    # Leer primera pestaña del excel (sheet_name=0) y guardar en DataFrame:
    xlsx = pd.ExcelFile(rutaArchivo)
    df1 = pd.read_excel(xlsx,sheet_name=0)

    # Reemplazar todos los NaN por -1
    df1 = df1.replace(np.nan,-1)
    
    # Guardar alumnos en lista, contar veces que alumno es mencionado como amigo o enemigo en dictAmigos:
    for alumno in df1.index:
        # Para el id, los amigos y los enemigos, se asegura de que se haga una conversión a int en caso de que sea float:
        if isinstance(df1["id"][alumno], float):
            id = str(int(df1["id"][alumno])).upper()
        else:
            id = str(df1["id"][alumno]).upper()
        nombre = df1["Nombre"][alumno]
        amigos = [0,0,0]
        enemigos = [0,0,0]

        # Amigos:
        for i in range(0,3):
            if isinstance(df1[1][alumno],float):
                amigos[i] = str(int(df1[i+1][alumno])).upper()
            else:
                amigos[i] = str(df1[i+1][alumno]).upper()

        # Enemigos:
        for i in range(0,3):
            if isinstance(df1[i+4][alumno],float):
                enemigos[i] = str(int(df1[i+4][alumno])).upper()
            else:
                enemigos[i] = str(df1[i+4][alumno]).upper()
        
        # Guardar en lista:
        listaAlu.append([id,nombre,amigos,enemigos])

        # Contar amigos y enemigos de cada alumno, guardar en diccionario:
        for amigo in amigos:
            if isinstance(amigo,str):
                if amigo in dictAmigos.keys():
                    dictAmigos[amigo] += 1
                else:
                  dictAmigos[amigo] = 1
        for enemigo in enemigos:
            if isinstance(enemigo,str):
                if enemigo in dictAmigos.keys():
                    dictAmigos[enemigo] -= 1
                else:
                    dictAmigos[enemigo] = -1
    return listaAlu, dictAmigos