# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 23:00:01 2020

@author: Gaurav
"""
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import random
import sys


#It  take voice from the windows
engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')

  
#Our pc  has 2 types of voice 0 is male nd 1 is female
engine.setProperty("voices", voices[1].id)
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
# voices = converter.getProperty('voices') 

engine.setProperty('rate', 150)

def sendemail(to,message):    
    
     server=smtplib.SMTP("smtp.gmail.com",587)
     server.ehlo()
     server.starttls()
     server.login("sinyash2000@gmail.com", "yashsing")
     server.sendmail("sinyash2000@gmail.com",to, message)
     server.close

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def wishme():
    #it give us the hour in 0 to 24
    hour=int(datetime.datetime.now().hour)
    if hour>=4 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<16:
        speak("Good afternoon")
    elif hour>=16 and hour<20:
        speak("Good evening")
    else:
        speak("Good night")
    
    speak(" Gaurav, I am your assistant David. How may i help you")
    

def takecommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query



if __name__=='__main__':
    wishme()
   
    while True:
        query=takecommand().lower()
        
        if "about" in query:
            speak("Searching")
            #query=query.replace("wikipedia","")
            result=wikipedia.summary(query, sentences=2)
            speak("According to me")
            print(result)
            speak(result)
            
        elif "open google" in query:
            speak("Opening google")
            webbrowser.open("google.com")

        elif "open youtube" in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")
        
        elif "open gmail" in query:
            speak("Opening gnail")
            webbrowser.open("gmail.com")
       
        elif "play music" in query or "play song" in query:
            r=random.randint(1,4)
            music_dir="D:\\Music"
            songs=os.listdir(music_dir)
            print(songs[r])
            os.startfile(os.path.join(music_dir,songs[r]))
        
        elif "time" in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            print(time)
            speak("The time is"+time)
            
        elif "open chrome" in query:
            path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)
        
        elif "stop" in query or "exit" in query:
            speak("Good bye, have a nice day")
            sys.exit()
        
        elif "email" in query:
            if "gaurav" in query:
                try:
                    print("What should I mail?")
                    speak("What should I mail?")
                    message=takecommand()
                    to="sintg1999@gmail.com"
                    sendemail(to,message)
                    print("Email has been sent sucesesfully")
                    speak("Email has been sent sucesesfully")
                except Exception as e:
                    print(e)
                    speak("Sorry some problem is occured.")
            elif "father" in query:
                try:
                    print("What should I mail?")
                    speak("What should I mail?")
                    message=takecommand()
                    to="sinarun1971@gmail.com"
                    sendemail(to,message)
                    print("Email has been sent sucesesfully")
                    speak("Email has been sent sucesesfully")
                except Exception as e:
                    print(e)
                    speak("Sorry some problem is occured.")  
                    
        elif "sujit" in query:
            speak("ooo Gattu he is your freind who run with his small legs.")
        
        elif "meera" in query:
            speak("Vo tumari mummy hai. She is your mother.")

        elif "Arun" in query:
            speak("Vo tumari papa hai. He is your father.")
            
                                    
                    
                    