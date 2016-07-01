#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        ModLeercsv
# Purpose:     Modulo encargado de recuperar datos del diccionario frases.csv
# Author:      Mauricio Jose Tobares
# Created:     06/05/2016
# Copyright:   (c) Mauricio 2016
# Licence:     <licencia?? que es eso??>
# Version:     0.0.01
#-------------------------------------------------------------------------------
# Modulo CSV de python
import csv
# Modulo operator de python
import operator
# Modulo GetPass
import getpass

def leerNotas(fraseNum):
# antes que nada creamos un diccionario vacio con el que trabajaremos
    diccionario = {}
# Crear nuevo dialecto llamado 'personal'
    csv.register_dialect('personal', delimiter='|', quotechar='"', quoting=csv.QUOTE_ALL)
# abrimos el archivo con el que trabajaremos
    with open('frases.csv') as csvarchivo:
        entrada = csv.reader(csvarchivo, dialect='personal')
        for datos in entrada:
            listadelistas = [(datos[0]),(datos[1]),(datos[2])]
            listadelistas = list(listadelistas)
            lista = str(listadelistas[1])
            diccionario[lista] = str(listadelistas[2])
# mensaje de voz
        return diccionario[fraseNum]
# es importante cerrar los archivos en cada bucle
    csvarchivo.close()
