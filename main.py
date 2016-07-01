#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        Asistente virtual con pyttsx
# Purpose:     El siguiente proyecto pretende crear un asistente personal basado
#              en pyttsx y python 2.7
# Author:      Mauricio Jose Tobares
# Created:     06/05/2016
# Copyright:   (c) Mauricio 2016
# Licence:     <licencia?? que es eso??>
# Version:     0.0.01
#-------------------------------------------------------------------------------
# Modulo os
import os
# Modulo RE
import re
# Modulo CSV de python
from csv import *
# Modulo operator de python
import operator
# Modulo de control hablar/escuchar creado por mi para el manejo de la voz
import ModVoz
# Modulo dialogos (este es el modulo que maneja el diccionario de dialogos)
import ModLeercsv
# Modulo time de python
import time
# Modulo GetPass
import getpass

def main():
    """ este es el inicio del programa y donde se retorna continuamente """
# traemos el dialogo de saludo
    frase1 = ModLeercsv.leerNotas('frase 1')
    frase2 = ModLeercsv.leerNotas('frase 2')
    usuario = getpass.getuser()
    holaUsuario = frase1+usuario+frase2
# hacemos que lea este mensaje
    ModVoz.hablar(holaUsuario)
# imrpimimos en la consola el mensaje
    print(holaUsuario)
# lo primero lo primero definimos como vacio nombre_de_la_funcion
#    nombre_de_la_funcion = ModVoz.escuchar()
    nombre_de_la_funcion = raw_input() # solo para testeos
# enviamos los datos a procesar a la siguiente funcion
    procesadorDeFunciones(nombre_de_la_funcion)

def procesadorDeFunciones(nombre_de_la_funcion):
    """ Esta funcion recibe un dato y comprueba si existe una funcion con ese
    nombre y la ejecuta, caso contrario entrega un mensaje al usuario informando
    de ello y dando una nueva opcion para una nueva tarea."""
# empecemos con RE, tomamos el valor que viene de main y la procesamos para
# saber que es lo que quiere el usuario (un poco adivinando porque a veces el
# asistente NO ENTIENDE muy bien lo que decimos y por tanto un poco de
# expresiones regulares soluciona en parte este problema

    re_nombre_de_la_funcion = re.search(r'(.*)abl(.*)', nombre_de_la_funcion)
    if re.search(r'trabaj', nombre_de_la_funcion) == nombre_de_la_funcion:
        nombre_de_la_funcion = 'trabajar'
    elif re.search(r'abla', nombre_de_la_funcion) == nombre_de_la_funcion:
        nombre_de_la_funcion = 'hablar'
    else:
# aca hay que agregar el NO ENTIENDO LO QUE DICES!!
        nombre_de_la_funcion = nombre_de_la_funcion

    if nombre_de_la_funcion in globals():
        if callable(globals()[nombre_de_la_funcion]):
            frase3 = ModLeercsv.leerNotas('frase 3')
            print(frase3,nombre_de_la_funcion)
            ModVoz.hablar(frase3)
            ModVoz.hablar(nombre_de_la_funcion)
# agregamos una espera de un segundo porque de no ser así pasaría directamente a
# ejecutar la funcion sin mostrar el mensaje por consola ni pronunciar el mensaje
            time.sleep(1)
# ejecutamos la funcion
            return globals()[nombre_de_la_funcion]()
    else:
        frase4a = ModLeercsv.leerNotas('frase 4 a')
        frase4b = ModLeercsv.leerNotas('frase 4 b')
        print(frase4a,nombre_de_la_funcion,frase4b)
        frase = str(frase4a)+str(nombre_de_la_funcion)+str(frase4b)
        ModVoz.hablar(frase)
        siono = ''
#        siono = ModVoz.escuchar()
        siono = raw_input('todavia no lo has programado, deseas programarlo? si o no: ') # solo para testeos
        if siono == 'si':
            frase5 = ModLeercsv.leerNotas('frase 5')
            print(frase5)
            ModVoz.hablar(frase5)
            time.sleep(1)
            return main()
        elif siono == 'no':
            frase6 = ModLeercsv.leerNotas('frase 6')
            print(frase6)
            ModVoz.hablar(frase6)
            time.sleep(1)
            return main()
        else:
            return main()

def hablar():
    """ funcion de ejemplo que solo dice \"hola\" y retorna al inicio """
    print "esto es una funcion que dice HOLA!!"
    dialogo = "esto es una funcion que dice HOLA!!"
    ModVoz.hablar(dialogo)

# creamos un retardo y devolvemos al inicio
#    time.sleep(1)
#    main()

def trabajar():
    """ esta funcion es un ejemplo de como se puede manejar un arbol de opciones
    y tomar decisiones segun corresponda """
    print('esto es tu oficina de trabajo, en que deseas trabajar?')
    ModVoz.hablar('esto es tu oficina de trabajo, en que deseas trabajar?')
# recojemos la informacion que nos brinda el usuario
    accion = raw_input('esto es tu oficina de trabajo, en que deseas trabajar? ')
    if accion == '': # si no escucha nada devolvemos al inicio
        main()
    elif accion == 'nada': # si el usuario no quiere hacer nada devolvemos al inicio
        main()
    elif accion == 'escribir':
# traemos el dialogo que se debe mostrar y decir
        frase = 'abriendo notepad'
        dialogo = ModLeercsv.leerNotas(frase)
        print(dialogo)
        ModVoz.hablar(dialogo)
# abrimos el notepad indicando la ruta hacia la aplicacion (no se como se hace en linux)
        os.system('C:\Windows\System32\notepad.exe')
# una vez lanzada la aplicacion creamos un retardo y devolvemos al inicio
#        time.sleep(1)
#        main()
    else: # si ninguna de las opciones anteriores se produce devolvemos al inicio
        main()

if __name__=='__main__':
    main()
## cuando el asistente diga "hola {usuario} en que puedo ayudarlo? podemos
## indicarle el nombre de la funcion que queremos que ejecute, en nuestro caso
## solo existen 2, trabajar y hablar, pero en las siguientes versiones se
## agregaran mas modulos para que el asistente sea mas util
