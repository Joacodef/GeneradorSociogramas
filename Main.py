from cgitb import text
import Excel
import Grafo
import PySimpleGUI as sg
import time
import os
import shutil

nombreHoja = ""

# Ventana para seleccionar el archivo excel donde se especifican amistades
def seleccionarArchivo():
    working_directory = os.getcwd()
    if os.path.isdir("doctest-output"):
        shutil.rmtree("doctest-output")
    layout = [
        [sg.Text("Seleccione Archivo: ")],
        [sg.InputText(key="rutaArchivo"),
        sg.FileBrowse(initial_folder=working_directory)],
        [sg.Button("Seleccionar"), sg.Button("Cancelar")]
    ]
    ventana = sg.Window('Elegir archivo', layout, element_justification='c')
    while True:
        event, values = ventana.read()    
        if event in [sg.WIN_CLOSED,'Cancelar']:
            break
        elif event in ['Seleccionar']:
            listaAlu, dictAmigos = Excel.generarListaDict(values["rutaArchivo"],nombreHoja)
            Grafo.generarGrafo(listaAlu, dictAmigos)
            if os.path.isdir("doctest-output"):
                layout2 = [[sg.Text("Se ha creado sociograma, revisar carpeta \"doctest-output\"")],[sg.Button("Aceptar")]]
            else:
                layout2 = [[sg.Text("Error en la creacion del sociograma, intentelo de nuevo")],[sg.Button("Aceptar")]]
            ventana2 = sg.Window('Resultado', layout2, element_justification='c')
            while True:
                event2, values2 = ventana2.read()
                if event2 in [sg.WIN_CLOSED,'Aceptar']:
                    break
            break


seleccionarArchivo()




"""
# Ventana principal
layout = [[sg.Text("¿Qué desea hacer?")], [sg.Button("Generar Sociograma")]]
ventana = sg.Window("Generador de Sociogramas", layout, margins=(100, 50))

while True:
    event, values = ventana.read()    
    if event == "Generar Sociograma":
        seleccionarArchivo()
        break
    elif event == sg.WIN_CLOSED:
        break
"""
