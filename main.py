# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        Asistente virtual con pyttsx
# Purpose:     El siguiente proyecto pretende crear un asistente personal basado
#              en python 3.x
# Author:      Mauricio José Tobares
# Created:     06/05/2016
# Copyright:   (c) Mauricio 2016
# Licence:     <licencia?? que es eso??>
# Version:     0.0.03
#-------------------------------------------------------------------------------
# se importa el modulo getpass que en windows sirve para averiguar el nombre
# del usuario pc
import getpass
# Modulo time de python, necesario para trabajar con tiempos
import time
#-------------------------------------------------------------------------------
# importamos los modulos propios necesarios y asignamos un alias adecuado
#-------------------------------------------------------------------------------
# el módulo controlAudio se utiliza para trabajar con la voz del asistente y
# tomar capturas del micrófono
from modulos.controlAudio import *
# el módulo hablar es el encargado de entablar conversación con el usuario y a
# la vez es el lugar donde se le pueden enseñar nuevos diálogos al asistente
from modulos.hablar import *
# import modulos.hablar as ModHablar
# el módulo leercsv se utiliza para trabajar con los archivos csv
from modulos.leercsv import *

def main(vuelta=0):
    ' Esta función es la entrada al programa. '
    """ La función main es la que se encarga de recibir al usuario y preguntarle
        que es lo que quiere hacer, si es la primera vez que el usuario enciende
        el asistente le dará la bienvenida, si no es así y ya se encuentra
        utilizando el asistente no le dará la bienvenida, simplemente le
        preguntará que quiere hacer """
    if vuelta == 0:
# traemos el dialogo de saludo
        frase1 = leerNotas('frase 1')  # modulos.leercsv.leerNotas
# asignamos el nombre del usuario pc a una variable para luego utilizarla
        usuario = getpass.getuser()
# segundo diálogo
        frase2 = leerNotas('frase 2')  # modulos.leercsv.leerNotas
# ahora lo que hacemos es unir la oración en un solo string para poder
# utilizarlo con mayor comodidad
        holaUsuario = frase1+usuario+frase2
    else:
# traemos el diálogo correspondiente (ya no saluda sino que pasa a dar opciones)
        frase1 = leerNotas('frase 1b')  # modulos.leercsv.leerNotas
        usuario = getpass.getuser()
        frase2 = leerNotas('frase 2b')  # modulos.leercsv.leerNotas
        holaUsuario = frase1+usuario+frase2  # unificamos la frase
# hacemos que el asistente lea el mensaje adecuado
    voz_asistente(holaUsuario)  # modulos.controlAudio.voz_asistente
# la función escuchar del modulo de voz todavía no funciona
#    nombre_de_la_funcion = escuchar()  # se comenta para testear / modulos.controlVoz.escuchar
    accion_requerida = input(holaUsuario)
# enviamos los datos a procesar a la siguiente funcion
    procesadorDeFunciones(accion_requerida)

def procesadorDeFunciones(accion_requerida):
    ' esta función es un pequeño arbol de decisiones. '
    """ A esta función llegan las decisiones que el usuario toma, la función
        analiza si la decisión es válida y procede a ejecutar el módulo que
        corresponda a dicha acción, caso contrario entrega un mensaje al usuario
        informando de ello y dando una nueva opción para una nueva tarea. """
    ejecutar = acciones(accion_requerida)  # modulos.leercsv.acciones
    """ todo programa tiene que tener una forma de detenerlo ya que de otra
        forma entraría en un bucle infinito y no es bueno que eso suceda """
    if 'terminar' in ejecutar:
        terminar()
    else:
        """ el siguiente if genera una función sin nombre, consulta al sistema si
            existe una función con el nombre requerido y lo ejecuta, caso contrario
            da aviso de ello al usuario """
        if ejecutar in globals():  # existe la funcion en modo global?
            if callable(globals()[ejecutar]):  # se puede acceder a dicha función?
                main(globals()[ejecutar]())  # ejecutamos la acción requerida y retornamos al inicio
        else:  # caso contrario utilizaremos este bloque para otras acciones
            """ en este bloque lo que haremos es en primera instancia crear un
            módulo que sea capaz de crear módulos básicos pidiendo al usuario los
            siguientes datos:
                nombre del módulo
                de que manera se llama al módulo (la frase con la que se invoca) """
            voz_asistente(r'Función no encontrada')  # se descomenta solo para testeos modulos.controlAudio.voz_asistente
            print(r"Función no encontrada")  # se descomenta solo para testeos
            main(ejecutar)  # retornamos al inicio

def terminar():
    voz_asistente(leerNotas('frase 10'))
    print(leerNotas('frase 10'))

if __name__=='__main__':
    main()
