import datetime
import wikipedia
import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import smtplib
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good Morning!")
    elif hour>=12 and hour <16:
        speak("Good Afternoon!")
    else:
        speak("Good evening!")
    speak("I am Striko Sir. Please tell me how I may help you.")

def takeCommand():
    '''
    it takes microphone input from the user and return and string outputs.
    ''' 
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")  
        r.pause_threshold = 1 
        r.energy_threshold = 1000
         
        audio= r.listen(source)

    try:
        print("Recognizing...")
        query= r.recognize_google(audio,language="en-in")
        print(f"User said : {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None" #it is string ye none wo wala nhi hai.
    return query
def sendEmail(to,content):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('jffhfdhkjfh@gmail.com','password-here')#Make turn on 'less secure app'option in ur given gmail.
    server.sendmail('jffhfdhkjfh@gmail.com',to,content)
    server.close()


    
    
if __name__ == "__main__":
    wishMe()
    while(True):
   #if 1:

        query=takeCommand().lower()
    #Logic for executive tasks based on query.
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace('wikipedia','')
            results= wikipedia.summary(query,sentences=2)
            speak("Acording to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir= "D:\\Music\\English"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0])) #use random module for random songs.

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath="C:\\Users\\parma\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email to striker' in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to="xhffdfdffdl@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak('Sorry Sir, I am not able to send this email')