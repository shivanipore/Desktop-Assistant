from math import e
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<=12):
        speak("Good Morning")
    
    elif hour>=12 and hour<=18:
        speak("Good Afternoon")
    
    else:
        speak("Good Evening")

    speak("Hello! I am Ruby. Please tell me how may I help you?")

def takeCommand():
    #It takes microphone input from the user and returns the string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio)
        print(f'User said: {query}\n')

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"

    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('poreshivani@gmail.com','Shivani@123')
    server.sendmail('poreshivani@gmail.com',to,content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences =2 )
            speak('According to Wikipedia')
            print(f'According to Wikipedia {results}')
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')


        elif 'open google' in query:
            webbrowser.open('youtube.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('youtube.com')

        elif 'open facebook' in query:
            webbrowser.open('youtube.com')

        elif 'play music' in query:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[random.randint(0,len(songs)-1)]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f'The time is {strTime}')

        elif 'open code' in query:
            codePath = "C:\\Users\\pores\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to summit' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'thakursumit1311@gmail.com'
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry your Email is not sent")

        elif 'play movie' in query:
            movie_dir = 'D:\\MOVIES'
            movies = os.listdir(movie_dir)
            print(movies)
            os.startfile(os.path.join(movie_dir,random.randint(0,len(movies)-1)))

        elif 'quit' or 'bye' in query:
            speak('Thankyou for your time.')
            print('Thankyou for your time.')
            exit()

        
