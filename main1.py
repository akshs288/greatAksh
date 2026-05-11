import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import os
import webbrowser
import random
import pywhatkit as pw  # For sending WhatsApp messages
import shutil
import sys

# Detect Chrome Path
def get_chrome_path():
    chrome_path = shutil.which('chrome') or "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    return chrome_path

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust speech rate

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Convert Voice to Text
def take():
    d = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        d.adjust_for_ambient_noise(source)
        d.pause_threshold = 1
        try:
            aud = d.listen(source, timeout=10, phrase_time_limit=4)
            print('Wait... Processing...')
            qe = d.recognize_google(aud, language='en-IN')
            print(f'You said: {qe}')
            return qe.lower()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
            return None
        except sr.RequestError:
            print("There was an issue connecting to the recognition service.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

# Greetings Based on Time
def greet():
    h = datetime.datetime.now().hour
    if 5 < h < 12:
        speak('Good morning, Sir. How can I help you?')
    elif 12 <= h < 16:
        speak('Good afternoon, Sir. How can I help you?')
    else:
        speak('Good evening, Sir. How can I help you?')

if __name__ == '__main__':
    get_chrome_path()
    greet()
    while True:
        query = take()
        if not query:
            continue
        
        # Open Websites
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")
        elif 'open netflix' in query:
            webbrowser.open("https://www.netflix.com")
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
        
        # Open Any Website Dynamically
        elif 'open' in query:
            site = query.replace('open ', '').strip()
            webbrowser.open(f"https://www.{site}.com")
            speak(f"Opening {site}")
        
        # Open Edit Folder and Play a Random File
        elif 'open edit' in query:
            folder_path = "D:\\aksh's all editz\\Editz"
            files = os.listdir(folder_path)
            if files:
                random_file = random.choice(files)
                os.startfile(os.path.join(folder_path, random_file))
            else:
                speak("No files found in the edit folder.")
        
        # Wikipedia Search
        elif 'wikipedia' in query:
            query = query.replace('wikipedia', '').strip()
            try:
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except wikipedia.exceptions.DisambiguationError:
                speak("There are multiple results, please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("No Wikipedia page found for this query.")
        
        # Google Search
        elif 'search' in query:
            query = query.replace('search', '').strip()
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Searching Google for {query}")
        
        # Open Google and Ask for Search Query
        elif 'turn on the google' in query:
            webbrowser.open("https://www.google.com")
            speak('What do you want to search on Google?')
            search_query = take()
            if search_query:
                webbrowser.open(f"https://www.google.com/search?q={search_query}")
                speak(f"Searching for {search_query}")
            else:
                speak("I couldn't hear you properly. Please try again.")
        
        # Send WhatsApp Message (Requires Web WhatsApp Logged In)
        elif 'open whatsapp' in query:
            try:
                pw.sendwhatmsg_instantly('+919650565718', 'Namaste')
                speak("Message sent successfully.")
            except Exception as e:
                print(f"Error sending WhatsApp message: {e}")
                speak("I encountered an issue sending the message.")
        
        # Exit Command
        elif 'exit' in query or 'no thanks' in query:
            speak('Thank you, sir. Have a nice day!')
            sys.exit()
        
        # Ask if the User Has More Queries
        speak('Sir, do you have any other query?')
