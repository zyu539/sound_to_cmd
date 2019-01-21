#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 13:03:47 2019

@author: lhy
"""

import wave, pylab as pl, numpy
import speech_recognition as sr

def audio2text(prompt_text, language=None):
    text = None
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print(prompt_text)
        audio = r.listen(source)
        
    try:        
        text = r.recognize_google(audio, language='zh-CN') if language else r.recognize_google(audio)
        print("Speech Recognition thinks you said " + text);        
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Speech Recognition service; {0}".format(e))
        
    return text.lower() if text else text 
    
        