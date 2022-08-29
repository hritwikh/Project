from datetime import datetime
from urllib.parse import SplitResult
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine= pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Greeting /Welcome message
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good eveing!")
    speak("Hello welcome to Stylish HRK World. How may I help you!!")

# Take microphone as input
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing.......")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said : {query}\n")
    except Exception as e:
        # print(e)
        print("say that again please...")
        return "None"
    return query

# Main function
if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        # Take action from online

        if 'wikipedia' in query:
            speak('searching wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening Youtube.......")
            webbrowser.open("https://www.youtube.com/watch?v=rKDRPVWtHuw")
        
        elif 'open google' in query:
            speak("Opening google.......")
            webbrowser.open("google.com")

        elif 'open gmail' in query:
            speak("Opening gmail.......")
            webbrowser.open("gmail.com")

        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir the time is {strTime} ")
        
        elif 'open channel'in query:
            speak("Opening channel plz wait!......")
            webbrowser.open("https://www.youtube.com/c/StylishHRK")

        elif 'end' in query:
            speak("Quiting sir!")
            break
        # else:
        #     speak("Ending")
        # break

