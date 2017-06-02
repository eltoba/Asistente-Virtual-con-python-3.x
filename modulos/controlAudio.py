# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        ControlAudio.py
# Purpose:     Como se trabajará en windows (por ahora) se utilizará para el
#              manejo de las voces win32com.client
# Author:      Mauricio José Tobares
# Created:     06/05/2016
# Copyright:   (c) Mauricio 2016
# Licence:     <licencia?? que es eso??>
# Version:     0.0.02
#-------------------------------------------------------------------------------
def voz_asistente(frase):
    ' Función que facilita la utilización de la voz del asistente. '
    """ Esta función lo que hace es, en primera medida cargar pyttsx como módulo
    propio, ya que este pyttsx es una modificación y adaptación para que
    funcione en python 3.x.
    A esta función se le pasa como argumento las frases que debe pronunciar el
    asistente. """
    import pyttsx
    engine = pyttsx.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voices', 'spanish')
    engine.setProperty('rate', 120)
    engine.say(frase)
    engine.runAndWait()
    print(frase)
