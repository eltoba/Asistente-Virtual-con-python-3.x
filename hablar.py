# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        hablar.py
# Purpose:     Este es un modulo de demostración de uso que ayuda a entablar una
#              conversacion con el asistente virtual y también facilita una
#              forma de ingresar nuevos diálogos al archivo dialogos.csv
# Author:      Mauricio Jose Tobares
# Created:     06/05/2016
# Copyright:   (c) Mauricio 2016
# Licence:     <licencia?? que es eso??>
# Version:     0.0.02
#-------------------------------------------------------------------------------
''' importamos el modulo "CSV" de python '''
import csv
''' módulo operator de python '''
import operator
''' módulo time de python '''
import time
# modulos propios
''' modulo leercsv '''
from leercsv import *
''' modulo controlAudio '''
from controlAudio import *

def dialogos(fraseNum):
# antes que nada creamos un diccionario vacio con el que trabajaremos
    diccionario = {}
# Crear nuevo dialecto llamado 'personal'
    csv.register_dialect('personal', delimiter='|', quotechar='"', quoting=csv.QUOTE_ALL)
# abrimos el archivo con el que trabajaremos
    with open('dialogos.csv') as csvarchivo:
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

def hablar(frase3=leerNotas('frase 3')):
    """ En este modulo se gestará un motor de dialogos con el cual se
    interactuara con el asistente virtual """
    voz_asistente(frase3)
    print(frase3)
    algo = input(frase3)
    voz_asistente('quieres hablar de '+algo+'??')
    time.sleep(1)
    return '1'

def escuchar():
    pass

def nuevoDialogo():
    """ En este modulo se gestará un motor de dialogos con el cual se
    interactuara con el asistente virtual indicandole nuevos dialogos, una vez
    aprendidos el asistente los podrá utilizar libremente """
# Crear nuevo dialecto 'personal' y abrir archivo usando dicho dialecto.
    csv.register_dialect('personal', delimiter='|',
        quotechar='"', quoting=csv.QUOTE_ALL)
# abrimos el archivo
    with open('dialogos.csv') as csvarchivo:
        lista1 = csv.reader(csvarchivo, dialect='personal')
        lista1 = list(lista1)
        i = len(lista1)
        numeroi = int(i)
        if numeroi <= 9:
            indice = '0'+str(numeroi)
        else:
            indice = str(numeroi)
# muestra el mensaje en audio
        voz_asistente(leerNotas('frase 4'))
# muestra el mensaje en la consola
        print(leerNotas('frase 4'))
# muestra el campo para ser llenado por el usuario
        clave = input(leerNotas('frase 4'))
# creamos un nuevo dialogo para el mensaje de audio
        creardialogo = leerNotas('frase 6')+clave
# muestra el mensaje en audio
        voz_asistente(creardialogo)
# mostramos el mensaje en la consola
        print(creardialogo)
# muestra el mensaje en audio
        voz_asistente(leerNotas('frase 5'))
# muestra el mensaje en la consola
        print(leerNotas('frase 5'))
# muestra el campo para ser llenado por el usuario
        valor = input(leerNotas('frase 5'))
# creamos un nuevo dialogo para el mensaje de audio
        creardialogo = leerNotas('frase 7')+valor
# muestra el mensaje en audio
        voz_asistente(creardialogo)
# mostramos el mensaje en la consola
        print(creardialogo)
# creamos una nueva lista
        lista2 = [[indice, clave, valor]]
# unimos ambas listas y las mostramos
        listaunida = lista1+lista2
# ordenamos la nueva lista según un campo determinado
        listaord = sorted(listaunida, key=operator.itemgetter(0), reverse=False)
# imprimimos la nueva lista en consola
        print(listaord)
# cerramos el archivo
    csvarchivo.close()
# Crear nuevo dialecto 'personal' y abrir archivo usando dicho dialecto.
    csv.register_dialect('personal', delimiter='|', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')
# abrimos el archivo
    csvsalida = open('dialogos.csv', 'w')
    salida = csv.writer(csvsalida, dialect='personal')
    for datos in listaord:
        salida.writerow(datos)
    del salida
    csvsalida.close()
# lo que hacemos a continuación es preguntar al usuario si quiere ingresar un
# nuevo dialogo, si la respuesta es afirmativa se vuelve a ejecutar esta función
# si la respuesta es negativa se vuelve al principio
    voz_asistente(leerNotas('frase 8'))
    print(leerNotas('frase 8'))
    respuestasiono = input(leerNotas('frase 8'))
    if respuestasiono == 'si':
        return 'si'
    elif respuestasiono == 'no':
        print(leerNotas('frase 9'))
        return 'no'
