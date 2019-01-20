#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 13:03:47 2019

@author: lhy
"""

import wave, pylab as pl, numpy
import speech_recognition as sr

def audio2text(prompt_text):
    text = None
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print(prompt_text)
        audio = r.listen(source)
        
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        text = r.recognize_google(audio)
        print("Google Speech Recognition thinks you said " + text);        
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        
    return text.lower() if text else text  
    
        