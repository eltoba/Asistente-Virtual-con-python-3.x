# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        Módulo leercsv
# Purpose:     Módulo encargado de recuperar datos del archivo frases.csv y
#              acciones.csv
# Author:      Mauricio José Tobares
# Created:     06/05/2016
# Copyright:   (c) Mauricio 2016
# Licence:     <licencia?? que es eso??>
# Version:     0.0.04
#-------------------------------------------------------------------------------
''' importamos el modulo "CSV" de python '''
import csv

def leerNotas(fraseNum):
    ' Esta función facilita el uso de csv '
    """ Esta función lo que hace es en primera medida crear un diccionario vacío
        luego lee el archivo csv correspondiente y lo carga al diccionario
        retornando el valor del mismo de la siguiente forma:
            diccionario[clave]=valor """
# antes que nada creamos un diccionario vacio con el que trabajaremos
    diccionario = {}
# Crear nuevo dialecto llamado 'personal' con el que está formateado el csv
    csv.register_dialect('personal', delimiter='|', quotechar='"', quoting=csv.QUOTE_ALL)
# abrimos el archivo con el que trabajaremos
    with open('frases.csv') as csvarchivo:
        entrada = csv.reader(csvarchivo, dialect='personal')
# en este bucle lo que hacemos es cargar los valores al diccionario vacío
        for datos in entrada:
            listadelistas = [(datos[0]),(datos[1]),(datos[2])]
            listadelistas = list(listadelistas)
            lista = str(listadelistas[1])
            diccionario[lista] = str(listadelistas[2])
# retornamos el valor del diccionario
        return diccionario[fraseNum]
# es importante cerrar los archivos en cada bucle
    csvarchivo.close()

def acciones(accionNum):
    ' se utiliza para trabajar con las acciones que puede realizar el usuario. '
    """ Es el mismo caso que la función leerNotas, solo que en lugar de leer el
        archivo de frases.csv se lee el archivo acciones.csv donde están
        registradas las acciones que puede realizar el usuario y retorna el
        valor del diccionario si existe, de lo contrario retorna '1' """
# antes que nada creamos un diccionario vacio con el que trabajaremos
    diccionario = {}
    keyexiste = {}
# Crear nuevo dialecto llamado 'personal' con el que está formateado el csv
    csv.register_dialect('personal', delimiter='|', quotechar='"', quoting=csv.QUOTE_ALL)
# abrimos el archivo con el que trabajaremos
    with open('acciones.csv') as csvarchivo:
        entrada = csv.reader(csvarchivo, dialect='personal')
# en este bucle lo que hacemos es cargar los valores al diccionario vacío
        for datos in entrada:
            listadelistas = [(datos[0]),(datos[1]),(datos[2])]
            listadelistas = list(listadelistas)
            lista = lista2 = str(listadelistas[1])
            diccionario[lista] = str(listadelistas[2])  # asignamos clave=valor
            keyexiste[lista2] = str(listadelistas[1])  # asignamos clave=clave
# comprobamos que el diccionario tenga la clave que le pasamos como argumento
    if accionNum in diccionario:
        return diccionario[accionNum]
# si no es así retornamos un '1'
    else:
        return '1'
# es importante cerrar los archivos en cada bucle
    csvarchivo.close()
