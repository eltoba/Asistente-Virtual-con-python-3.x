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
from modulos.leercsv import *
''' modulo controlAudio '''
from modulos.controlAudio import *

def dialogos(fraseNum):
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
    with open('csv/dialogos.csv') as csvarchivo:
        entrada = csv.reader(csvarchivo, dialect='personal')
# en este bucle lo que hacemos es cargar los valores al diccionario vacío
        for datos in entrada:
            listadelistas = [(datos[0]), (datos[1]), (datos[2])]
            listadelistas = list(listadelistas)
            lista = str(listadelistas[1])
            diccionario[lista] = str(listadelistas[2])
# averigua si la clave fraseNum está dentro del diccionario
    if fraseNum in diccionario:
        print(diccionario[fraseNum])  # se descomenta solo para testeos
        return diccionario[fraseNum]
# si la clave fraseNum no se encuentra en el diccionario retorna un valor vacio
    else:
        print(r'no existe ese diálogo')  # se descomenta solo para testeos
        return ''
# es importante cerrar los archivos en cada bucle
    csvarchivo.close()

def hablar(vuelta='0'):
    ' Módulo dedicado a la interacción usuario-asistente mediante diálogos '
    """ En este modulo se gestará un motor de diálogos con el cual se
    interactuará con el asistente virtual, cuanto mas se le enseñe mas diálogos
    conocerá. """
# este if sirve como método de control
    if vuelta == '0':
# el asistente pregunta de que quieres hablar
        voz_asistente(leerNotas('frase 3'))
        print(leerNotas('frase 3'))  # se descomenta solo para testeos
# se recolecta información del usuario (de que quiere hablar el usuario)
        tema = input(leerNotas('frase 3'))
# si el tema del que desea hablar el usuario existe
        retorno = dialogos(tema)
        if retorno != '':
#            voz_asistente(r'el diálogo ' + tema + ' existe')  # se descomenta solo para testeos
#            print(r'el diálogo ' + tema + ' existe')  # se descomenta solo para testeos
            time.sleep(1)
            voz_asistente(r''+dialogos(tema))
# si el tema del que desea hablar el usuario NO existe
        elif retorno == '':
# formamos el diálogo forzando el uso de acentos
            frase = leerNotas(r'frase 11')
# formamos el diálogo forzando el uso de acentos
            frase2 = r'el diálogo '+tema+' NO existe'
# el asistente no sabe que contestar y cuestiona al usuario para saber que decir
            voz_asistente(frase)  # LEER NOTA 1
            print(frase2)  # se descomenta solo para testeos
# el usuario debe decidir si desea programar una nueva respuesta o no
            recolector = input(r''+str(leerNotas('frase 11')))
            print(recolector)  # se descomenta solo para testeos
# si el usuario decide que efectivamente desea programar una respuesta al tema
# se lo envía al módulo de crear nuevos diálogos
            if recolector=='si' or recolector=='SI' or recolector=='Si' or recolector=='sI':
                nuevoDialogo()
# si el usuario decide que no es conveniente programar una respuesta se vuelve a
# iniciar el módulo de hablar pero esta vez desde la vuelta 1
# (ya no dará la bienvenida)
            elif recolector=='no' or recolector=='NO' or recolector=='No' or recolector=='nO':
                hablar(vuelta='1')
# si el usuario ya realizó un diálogo y retorna al módulo se partirá desde este
# punto y no desde todo lo anterior
    elif vuelta == '1':
# el asistente pregunta de que quieres hablar
        voz_asistente(leerNotas('frase 3'))
        print(leerNotas('frase 3'))  # se descomenta solo para testeos
# se recolecta información del usuario (de que quiere hablar el usuario)
        tema = input(leerNotas('frase 3'))
# si el tema del que desea hablar el usuario existe
        retorno = dialogos(tema)
        if retorno != '':
#            voz_asistente(r'el diálogo ' + tema + ' existe')  # se descomenta solo para testeos
#            print(r'el diálogo ' + tema + ' existe')  # se descomenta solo para testeos
            time.sleep(1)
            voz_asistente(r''+dialogos(tema))
# si el tema del que desea hablar el usuario NO existe
        elif retorno == '':
# el asistente no sabe que contestar y cuestiona al usuario para saber que decir
            voz_asistente(r''+str(leerNotas('frase 11')))  # LEER NOTA 1
            print(r'el diálogo '+tema+' NO existe')  # se descomenta solo para testeos
# el usuario debe decidir si desea programar una nueva respuesta o no
            recolector = input(r''+leerNotas('frase 11'))
            print(recolector)  # se descomenta solo para testeos
# si el usuario decide que efectivamente desea programar una respuesta al tema
# se lo envía al módulo de crear nuevos diálogos
            if recolector=='si' or recolector=='SI' or recolector=='Si' or recolector=='sI':
                nuevoDialogo()
# si el usuario decide que no es conveniente programar una respuesta se vuelve a
# iniciar el módulo de hablar pero esta vez desde la vuelta 1
# (ya no dará la bienvenida)
            elif recolector=='no' or recolector=='NO' or recolector=='No' or recolector=='nO':
                return 'no'  # devuelta al inicio
#                hablar(vuelta='1')

#    voz_asistente('quieres hablar de '+algo+'??')
    time.sleep(1)
    return '1'

def nuevoDialogo():
    """ En este modulo se gestará un motor de dialogos con el cual se
    interactuara con el asistente virtual indicandole nuevos dialogos, una vez
    aprendidos el asistente los podrá utilizar libremente """
# Crear nuevo dialecto 'personal' y abrir archivo usando dicho dialecto.
    csv.register_dialect('personal', delimiter='|',
        quotechar='"', quoting=csv.QUOTE_ALL)
# abrimos el archivo
    with open('csv/dialogos.csv') as csvarchivo:
        lista1 = csv.reader(csvarchivo, dialect='personal')
        lista1 = list(lista1)
# contamos el número de registros
        i = len(lista1)
# convertimos el numero de registros en un número natural para poder trabajarlo
        numeroi = int(i)
# si es un numero 0, 1 ... 9 se le agrega un cero a la izquierda
        if numeroi <= 9:
# creamos la nueva cadena 01, 02, 03 etc
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
    csvsalida = open('csv/dialogos.csv', 'w')
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
# NOTA 1: r'' se utiliza para indicar que DEBE forzar la utilización de utf-8
