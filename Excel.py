from cmath import isnan
import pandas as pd
import os
import math

def generarListaDict(rutaArchivo, nombrePestaña):
    # Setear cwd en el directorio del archivo actual
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    #print(os.getcwd())

    # xlsx = pd.ExcelFile('2021 NOVIEMBRE IERO MEDIO.xlsx')
    xlsx = pd.ExcelFile(rutaArchivo)
    # Leer pestañas del excel: Probablemente haya que cambiarle los nombres
    #df1 = pd.read_excel(xlsx,nombrePestaña)
    df1 = pd.read_excel(xlsx,sheet_name=0)

    listaAlu = []
    dictAmigos = dict()
    #dictEnemigos = dict()
    # Guardar alumnos en lista, contar veces que alumno es mencionado como amigo en dictAmigos:

    for alumno in df1.index:
        id = str(int(df1["id"][alumno])).upper()
        nombre = df1["Nombre"][alumno]
        amigos = [0,0,0]
        enemigos = [0,0,0]
        if not math.isnan(df1[1][alumno]):
            amigos[0] = str(int(df1[1][alumno])).upper()
        if not math.isnan(df1[2][alumno]):
            amigos[1] = str(int(df1[2][alumno])).upper()
        if not math.isnan(df1[3][alumno]):
            amigos[2] = str(int(df1[3][alumno])).upper()
        if not math.isnan(df1[4][alumno]):
            enemigos[0] = str(int(df1[4][alumno])).upper()
        if not math.isnan(df1[5][alumno]):
            enemigos[1] = str(int(df1[5][alumno])).upper()
        if not math.isnan(df1[6][alumno]):
            enemigos[2] = str(int(df1[6][alumno])).upper()
        listaAlu.append([id,nombre,amigos,enemigos])
        # Contar amigos y enemigos:
        # (Definir si queremos diccionarios distintos, o el mismo)
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
        
    """
        for enemigo in enemigos:
            if isinstance(enemigo,str):
                if enemigo in dictEnemigos.keys():
                    dictEnemigos[enemigo] += 1
                else:
                    dictEnemigos[enemigo] = 1
    for alu in listaAlu:
        print(alu)

    print("\n")"""
    #print(dictAmigos)
    return listaAlu, dictAmigos