# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        ControlVoz.py
# Purpose:     Como se trabajará en windows (por ahora) se utilizará para el
#              manejo de las voces win32com.client
# Author:      Mauricio José Tobares
# Created:     06/05/2016
# Copyright:   (c) Mauricio 2016
# Licence:     <licencia?? que es eso??>
# Version:     0.0.02
#-------------------------------------------------------------------------------
# modulo win32com.client de python para utilizar tts de windows
import win32com.client

def voz_asistente(frase):
    ' Función que facilita la utilización de la voz del asistente. '
    """ Esta función lo que hace es cargar el driver necesario para utilizar el
        tts en sistemas windows y se le pasan como argumentos las frases que
        debe pronunciar el asistente """
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(frase)

def escuchar():
    pass
