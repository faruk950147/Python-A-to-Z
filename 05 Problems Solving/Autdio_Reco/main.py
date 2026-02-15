import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import requests
import pyjokes
import os

# =======================
# Initialize speech engine
# =======================
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# =======================
# Greet user
# =======================
def greet_user():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your assistant. How can I help you today?")

# =======================
# Listen to user
# =======================
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-US')
        print(f"User said: {query}")
    except Exception:
        print("Sorry, I didn't catch that. Please say again.")
        return None
    return query.lower()

# =======================
# Weather function
# =======================
def get_weather(city):
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if data["cod"] != 200:
            speak(f"City {city} not found.")
            return
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        speak(f"The temperature in {city} is {temp} degree Celsius with {desc}")
    except:
        speak("Unable to get weather information right now.")

# =======================
# Main functionality
# =======================
def run_assistant():
    greet_user()
    while True:
        query = take_command()
        if query is None:
            continue
        
        # Exit
        if 'exit' in query or 'quit' in query:
            speak("Goodbye!")
            break

        # Time
        elif 'time' in query:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {time}")

        # Date
        elif 'date' in query:
            date = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today is {date}")

        # Open websites
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")
        
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            speak("Opening Google")

        # Wikipedia search
        elif 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            try:
                result = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(result)
            except:
                speak("Sorry, I could not find information on Wikipedia.")

        # Google search
        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Searching for {query}")

        # Weather
        elif 'weather' in query:
            speak("Please tell me the city name.")
            city = take_command()
            if city:
                get_weather(city)

        # Joke
        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        # Open desktop apps
        elif 'open notepad' in query:
            os.system('notepad')
            speak("Opening Notepad")
        
        elif 'open calculator' in query:
            os.system('calc')
            speak("Opening Calculator")

        else:
            speak("I can not do that yet.")

# =======================
# Run the assistant
# =======================
if __name__ == "__main__":
    run_assistant()
