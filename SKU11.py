import speech_recognition as sr


import webbrowser as wb
import logging

import pywhatkit as kittycat
import wikipedia

from ursina import *

import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")



def MainProg():
    speaker.Speak("SKU11 Module sucessfully initiated")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while True:


            print('listening')
            logging.info("Accessing Microphone.If Command Fails, Check Mic Privacy Settings.")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            try:
                com = ""
                com = r.recognize_google(audio)

                print(com)
                lis = list(com.split(" "))
                # if 'youtube' or 'Youtube' in lis:
                # speaker.Speak('Opening Youtube')
                # wb.open('https://www.youtube.com/')

                if 'Youtube' and 'open' in lis:
                    speaker.Speak('Opening Youtube')
                    wb.open('https://www.youtube.com/')
                elif "play" in lis:
                    zor = com
                    res = zor.replace("play", "")
                    speaker.Speak("Playing " + res)
                    kittycat.playonyt(zor)
                elif 'exit' in lis:
                    speaker.Speak('Goodbye')

                else:
                    try:
                        cattykit = wikipedia.summary(com,1)
                        speaker.Speak(cattykit)
                        print(cattykit)

                        print('Excecute next function')
                    except wikipedia.DisambiguationError or wikipedia.PageError:
                        c = "Could Not Find What You Requested"
                        speaker.Speak(c)
                        print(c)






            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))


