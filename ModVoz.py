#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        ModVoz.py
# Purpose:     Esta es la función que maneja la librería pyttsx
# Author:      Mauricio Jose Tobares
# Created:     06/05/2016
# Copyright:   (c) Mauricio 2016
# Licence:     <licencia?? que es eso??>
# Version:     0.0.01
#-------------------------------------------------------------------------------
# import speech_recognition as sr
import speech_recognition
# importamos el modulo pyttsx
import pyttsx

def hablar(frase):
    engine = pyttsx.init()
    voices = engine.getProperty('voices')
# definimos el idioma (es recomendable revisar que idioma tiene nuestro sistema)
    engine.setProperty('voice', "spanish-latin-american")
# es la velocidad con la que habla nuestro locutor o locutora :)
    engine.setProperty('rate', 120)
# aqui viene a parar la frase hola 'usuario' que desea hacer hoy? o lo que sea
    engine.say(frase)
    engine.runAndWait()

recognizer = speech_recognition.Recognizer()
def escuchar():
    with speech_recognition.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except speech_recognition.UnknownValueError:
        print("Could not understand audio")
    except speech_recognition.RequestError as e:
        print("Recog Error; {0}".format(e))
    return ""
