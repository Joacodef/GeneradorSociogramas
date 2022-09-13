import pandas as pd
import os


def generarListaDict(rutaArchivo, nombrePestaña):
    # Setear cwd en el directorio del archivo actual
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    print(os.getcwd())

    # xlsx = pd.ExcelFile('2021 NOVIEMBRE IERO MEDIO.xlsx')
    xlsx = pd.ExcelFile(rutaArchivo)
    # Leer pestañas del excel: Probablemente haya que cambiarle los nombres
    df1 = pd.read_excel(xlsx,nombrePestaña)

    listaAlu = []
    dictAmigos = dict()
    dictEnemigos = dict()

    # Guardar alumnos en lista, contar veces que alumno es mencionado como amigo en dictAmigos:

    for alumno in df1.index:
        id = str(df1["id"][alumno]).upper()
        nombre = df1["Nombre"][alumno]
        amigos = [0,0,0,0]
        enemigos = [0,0,0]
        amigos[1] = str(df1[1][alumno]).upper()
        amigos[2] = str(df1[2][alumno]).upper()
        amigos[3] = str(df1[3][alumno]).upper()
        enemigos[0] = str(df1[4][alumno]).upper()
        enemigos[1] = str(df1[5][alumno]).upper()
        enemigos[2] = str(df1[6][alumno]).upper()
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
                    dictEnemigos[enemigo] = 1"""
                    
    return listaAlu, dictAmigos