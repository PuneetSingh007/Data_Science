import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import subprocess as sp
import pywhatkit as kit
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio) :
    engine.say(audio)
    engine.runAndWait()
    
    
def wishme() : 
     hour = int(datetime.datetime.now().hour)
     if hour>=0 and hour<12 :
           speak("Good Morning Sir!")
           
     elif hour>=12 and hour<18 :
           speak("Good Afternoon Sir!")
           
     else :
           speak("Good Evening Sir")
           
     speak("I am Jarvis . Please tell me how do I  help you")
     
     
def takeCommand() :
  #It takes microphone input from the user and returns string output
  
  r = sr.Recognizer()
  with sr.Microphone() as source :
    print("Listening")
    r.pause_threshold = 1
    audio = r.listen(source)
    
  try :
    print("Recognising ")
    query = r.recognize_google(audio, language='en-in')
    print(f"User said : {query}\n")
    
  except Exception as e :
    #print(e)
    print("Say that again please...")
    return "None"
  return query

def open_camera() :
    sp.run('start microsoft.windows.camera:' , shell =True)
      
def get_random_joke():
    headers = {
      'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]
           
     
def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']


def play_on_youtube(video) :
      kit.playonyt(video)

def search_on_google(search) :
      kit.search(search)
        
def send_whatsapp_message() :
      kit.sendwhatmg_instantly(f"+91{number}", message)
      
def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]
     
     
if _name_ == "_main_" :
      wishme()
      value = 1
      while (value==1) :
            query = takeCommand().lower()
             
             # Logic for executing tasks based on query 
            if 'wikipedia' in query :
                  speak('Searching wikipedia...')
                  query = query.replace("on wikipedia", "")
                  results = wikipedia.summary(query,sentences=5)
                  speak("According to wikipedia")
                  print(results)
                  speak(results)
                  speak("For your convenience I am printing it on the screen sir")
            
            elif 'youtube' in query:
                  speak('What do you want to play on Youtube, sir?')
                  video = takeCommand().lower()
                  play_on_youtube(video)
 
 
            elif "send whatsapp message" in query:
                  speak('On what number should I send the message sir? Please enter in the console: ')
                  number = input("Enter the number: ")
                  speak("What is the message sir?")
                  send_whatsapp_message(number, message)
                  message = takeCommand().lower()
                  speak("I've sent the message sir.")
                 
            elif 'joke' in query:
                  speak(f"Hope you like this one sir")
                  joke = get_random_joke()
                  speak(joke)
                  speak("For your convenience, I am printing it on the screen sir.")
                  print(joke)   
                 
            elif "advice" in query:
                 speak(f"Here's an advice for you, sir")
                 advice = get_random_advice()
                 speak(advice)
                 speak("For your convenience, I am printing it on the screen sir.")
                 print(advice)
                                                
            elif 'search on google' in query:
                 speak('What do you want to search on Google, sir?')
                 search = takeCommand().lower()
                 search_on_google(search)         
                 
  
            elif 'open google' in query :
                  webbrowser.open("google.com")
                  
            elif 'open stackoverflow' in query :
                  webbrowser.open("stackoverflow.com")
                  
            elif 'play music' in query :
                  music_dir = 'C:\\Users\\punee\\Music'
                  songs = os.listdir(music_dir)
                  print(songs)
                  os.startfile(os.path.join(music_dir, songs[0]))
                  
            elif 'the time' in query :
                  strTime = datetime.datetime.now().strftime("%H:%M:%S")
                  speak(f"Sir the time is {strTime}")
             
            elif 'yourself' in query :
                  speak("My Name is Jarvis and I am basically a assistant. You can call me a small example of AI")
                  speak("My full form is just a rather very intellient system.")
                  print("My Name is Jarvis and I am basically a assistant. You can call me a small example of AI")
                  print("My full form is just a rather very intellient system.")
                             
            elif 'open camera' in query:
                    open_camera()    
            
            elif 'quit' in query :
                  value = 0