

import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary  # Ensure this module and 'music' dictionary are properly defined
import requests


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "3a8bc4e78adc417aa7a5a302dec2daca"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://whatsapp.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        try:
            link = musiclibrary.music[song]
            webbrowser.open(link)
        except KeyError:
            speak("Sorry, I couldn't find that song in the library.")

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the json responce
            data = r.json()

            # Extract the articles.
            articles = data.get("articles",[])

            # Print the headlines
            for article in articles:
                speak(article['title'])


if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
                word = recognizer.recognize_google(audio)
                
            if "jarvis" in word.lower():
                speak("Yes, how can I help?")
                print("Jarvis activated...")
                
                # Listen for command
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=1)
                    print("Listening for command...")
                    audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
                    command = recognizer.recognize_google(audio)  # Changed from 'recognize_bing' to 'recognize_google'
                    print(f"Command received: {command}")
                    processCommand(command)

        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Please try again.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"Error: {e}")
