import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser as wb
import requests
import json
import pywhatkit
import wikipedia
import pyjokes
import PIL
import smtplib

base_url="https://api.openweathermap.org/data/2.5/weather?"
api_key="efcaf47a78df5a3ae48c649969526169"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',170)

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
        speak("Good Evening!")  
        
    print("I am Jarvis Sir. Please tell me how may I help you")
    speak("I am Jarvis Sir. Please tell me how may I help you")

    
    
def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source,0,5)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-US")
        print(f"You Said : {query}")
    except:
        return ""

    return query

wishMe()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('aiassitant.jarvis@gmail.com', 'tjjjokvbafczmgro')
    server.sendmail('aiassitant.jarvis@gmail.com', to, content)
    server.close()

def Main():

    query = Listen().lower()
        
    if 'wikipedia' in query:
            #speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            #speak("According to Wikipedia")
            print(results)
            speak(results)
            
    elif "news" in query:
        speak("Today's News")
        a=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=f6db5e88148d468aa2237314761068c5")
        b=json.loads(a.text)
        for i in range(5):
            dataa=b['articles'][i]['title']
            print ("Title:",i+1,dataa)
            speak(dataa)
                
    elif 'date' in query:
        date = datetime.datetime.now().strftime('%d %b %Y')
        print(date)
        speak(date)

    elif 'time' in query:
        time = datetime.datetime.now().strftime('%I:%m %p')
        print(time)
        speak(time)
            
    elif 'day' in query:
        day = datetime.datetime.now().strftime("%A")
        print(day)
        speak(day)

    elif "are you single" in query:
        speak("Personal question, but let me tell you. i'm in relationship with wi-fi")
            
    elif 'open youtube' in query:
        speak("opening youtube")
        print("opening youtube")
        url1="https://www.youtube.com/"
        wb.open(url1)
            
    elif 'open google' in query:
        url2="https://www.google.co.in/"
        wb.open(url2)
            
    elif 'play on youtube' in query:
        query=query.replace("play on youtube","")
        speak("Playing")
        pywhatkit.playonyt(query)
            
    elif 'google search' in query:
        query=query.replace('google search','')
        query=query.replace(' ','+')
        url3="https://www.google.com/search?q="
        ser=url3+query
        speak("Searching")
        wb.open(ser)
        
    elif "temperature" in query:
        city_name=str(query.split()[-1:][0])
        print(city_name)
        complete_url = base_url + "q=" + city_name + "&appid=" + api_key
        response = requests.get(complete_url) 

        x = response.json() 
        if x["cod"] != "404": 
            y = x["main"] 
            current_temperature = y["temp"] 
            current_pressure = y["pressure"] 
            current_humidiy = y["humidity"] 
            z = x["weather"] 
            weather_description = z[0]["description"] 
            print(" Temperature (in Celcius unit) = " +
                            str(int(current_temperature)-273.15) + 
                  "\n atmospheric pressure (in hPa unit) = " +
                            str(current_pressure) +
                  "\n humidity (in percentage) = " +
                            str(current_humidiy) +
                  "\n description = " +
                            str(weather_description))
            speak(" Temperature (in Celcius unit)  " +
                            str(int(current_temperature)-273.15) + 
                  "\n atmospheric pressure (in hPa unit)  " +
                            str(current_pressure) +
                  "\n humidity (in percentage)  " +
                            str(current_humidiy) +
                  "\n  " +
                            str(weather_description))
        else: 
            speak(" City Not Found ") 
        
    elif 'what is your name' in query:
        print("I'm Jarvis")
        speak("I'm Jarvis")

        
    elif 'hello' in query:
        speak("hello sir")
    
    elif 'how are you' in query:
        speak("perfect, what about you sir")
        
    elif 'i am fine' in query:
        speak("good to know, what should i do for you sir")
    
    elif "who created you" in query:
        print("Mr. Akshat")
        speak("Mister Akshat Gupta")
        
    elif "introduce yourself" in query:
        speak("I'm an AI Assistant of Mister Akshat Gupta   named JARVIS. speed ten zettaBytes. Memory 20 YottaBytes. ")
        
    elif "turn on the light" in query:
        print("Turning on")
        speak("Turning on")
        url4="http://188.166.206.43/085b9b57c39b480ab1d7bca27ee5ffe5/update/D16?value=0"
        wb.open(url4)
        
    elif "turn off the light" in query:
        print("Turning off")
        speak('Turning off')
        url5="http://188.166.206.43/085b9b57c39b480ab1d7bca27ee5ffe5/update/D16?value=1"
        wb.open(url5)
        
    elif "switch on" in query:
        speak("turning on")
        url6="http://188.166.206.43/085b9b57c39b480ab1d7bca27ee5ffe5/update/D5?value=0"
        wb.open(url6)
        
    elif "switch off" in query:
        speak("turning off")
        url7="http://188.166.206.43/085b9b57c39b480ab1d7bca27ee5ffe5/update/D5?value=1"
        wb.open(url7)
        
    elif "joke" in query:
        j=pyjokes.get_joke()
        print(j)
        speak(j)
        
    elif "send email" in query:
        try:
            speak("What should I say?")
            content = Listen()
            to = "akshat98770@gmail.com"    
            sendEmail(to, content)
            print("Email has been sent!")
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            speak("Sorry Boss. I am not able to send this email") 
    
    elif "what can you do" in query:
        print("Features of Jarvis includes the following: it can send emails, play music, google search, play anything on youtube, wikipedia searches, read news, give weather report, control home lights and fans etc.")
        speak("I can perform several human tasks with efficiency. like I can send emails, play music for you, i can google search anything, i can do wikipedia searches, i can also read today's news, i can give you today's weather report, and most importantly i can control your home lights & fans etc.")
        
    elif "goodbye" in query:
        speak("bye sir, nice to meet you")
        exit()
        

while True:
    Main()
