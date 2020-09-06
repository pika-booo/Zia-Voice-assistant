import pyttsx3
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import wolframalpha
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good evening!")

    speak("I am zia. How may I help you")
              
def takeCommand():
    #it take microphone user from user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recogninsing...")
        r.pause_threshold = 0.5
        query = r.recognize_google(audio, language='en-ln')
        print(f"user said:{query}\n")
        
    except Exception as e:
        print("Say that again Please..")
        return "None"
    return query
    
if __name__ == "__main__":
              wishMe()
              while True:
                  query = takeCommand().lower()

                  if 'wikipedia' in query:
                      speak('Searching wikipedia..')
                      query = query.replace("Wikipedia", "")
                      results = wikipedia.summary(query, sentences=2)
                      speak("According to Wikipedia")
                      print(results)
                      speak(result)
                  elif 'open youtube' in query:
                      webbrowser.open("youtube.com")
                      
                  elif 'open google' in query:
                      webbrowser.open("google.com")

                  elif 'open facebook' in query:
                      webbrowser.open("facebook.com")
                      
                    
                  elif 'play music' in query:
                      music_dir = 'F:\\phone songs'
                      songs = os.listdir(music_dir)
                      random = os.startfile(os.path.join(music_dir,songs[1]))
                  elif 'the time' in query:
                      strTime = datetime.datetime.now().strftime("%H:%M:%S")
                      speak(f"Prachi, the time is{strTime}")
                      print(strTime)
                  elif 'open vs code' in query:
                      codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
                      os.startfile(codePath)
                  elif 'how are you' in query:
                      speak("I am fine, Thank you")
                      speak("How are you, Prachi")
            
                  elif "what's your name" in query or "what is your name" in query:
                      speak("My friends call me zia")
                  elif 'fine' in query or "good" in query:
                      speak("It's good to know that your fine") 

                  elif 'exit' in query:
                      speak("Thanks for giving me your time") 
                      exit()
             
  
                  elif "who made you" in query or "who created you" in query:
                      speak("I have been created by Prachi.") 
              
                  elif 'joke' in query:
                      speak(pyjokes.get_joke()) 
              
                  elif "calculate" in query:
                      app_id = "Wolframalpha api id"
                      client = wolframalpha.Client(app_id)
                      indx = query.lower().split().index('calculate')
                      query = query.split()[indx + 1:]
                      res = client.query(' '.join(query))
                      answer = next(res.results).text
                      print("The answer is " + answer)
                      speak("The answer is " + answer)  
  
                  elif 'search' in query or 'play' in query:
                      query = query.replace("search", "")
                      query = query.replace("play", "")
                      webbrowser.open(query)  
  
                  elif "who i am" in query:
                      speak("If you talk then definately your human.") 
  
                  elif "why you came to world" in query:
                      speak("Thanks to Prachi. further It's a secret")

                  elif "will you be my girlfriend" in query or "will you be my bf" in query:
                      speak("I'm not sure about, may be you should give me some time") 
  
                  elif "how are you" in query:
                      speak("I'm fine, glad you me that") 
  
                  elif "i love you" in query:
                      speak("It's hard to understand") 
