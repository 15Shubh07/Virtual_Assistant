import pyttsx3
import speech_recognition as sh
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib

while True:
    engine=pyttsx3.init("sapi5")
    voices=engine.getProperty("voices")
    engine.setProperty("voice",voices[0].id)


    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def wishMe():
        hour=int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning")
        elif hour>=12 and hour<18:
            speak("Good Afternoon")
        else:
            speak("Good Evening")

        speak("Hello sir. I am jarvis. How may I help you")




    def takeCommand():
        #it take input from microphone and return string output
        r = sh.Recognizer()
        with sh.Microphone() as source:
            print("Listning...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio,language="en-in")
            print(f"user said : {query}\n")
        except Exception:
            print("Say that again please..")
            return "none"
        return query

    def sendEmail(to,content):
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()
        server.starttls()
        speak("Please enter send email i d password")
        b=input("Enter password -> ")
        server.login("shubhsaxena1507@gmail.com",b)
        server.sendmail("shubhsaxena1507@gmail.com",to,content)
        server.close()

    if __name__=="__main__":
        wishMe()
        while True:
            query=takeCommand().lower()
        #logic for executing taskon query
            if "wikipedia" in query:
                speak("Searching wikipedia")
                query=query.replace("wikipedia","")
                results=wikipedia.summary(query,sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)
            elif "open youtube" in query:
                webbrowser.open("Youtube.com")
            elif "open google" in query:
                webbrowser.open("google.com")
            elif "open gmail" in query:
                webbrowser.open("gmail.com")
            elif "open facebook" in query:
                webbrowser.open("facebook.com")
            elif "open flipkart" in query:
                webbrowser.open("flipkart.com")
            elif "open amazon" in query:
                webbrowser.open("amazon.com")
            elif "play music" in query:
                music_dir="C:\\Users\\HP\\Desktop\\Music"
                songs=os.listdir(music_dir)
                # print(songs)
                b=len(songs) 
                a=random.randint(0,b-1)
                os.startfile(os.path.join(music_dir,songs[a])) 
            elif "time" in query:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir,the time is {strTime}")      
            elif "Open vs code" in query:
                code_path="C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(code_path)
            elif "dev c plus plus" in query:
                code_path="C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
                os.startfile(code_path)
            elif "open whatsapp" in query:
                code_path="C:\\Users\\HP\\Desktop\\WhatsApp"
                os.startfile(code_path)
            elif "email" in query:
                try: 
                    speak("Please Enter reciever email i d")
                    a=input("Enetr email id -> ")
                    speak("What should I say")
                    content=takeCommand()
                    to=a
                    sendEmail(to,content)
                    speak("Email has been sent succefuly")
                except Exception as e:
                    print(e)
                    speak("Sorry sir email is not sent")
            elif "quit" in query:
                hour=int(datetime.datetime.now().hour)
                if hour>=0 and hour<=16:
                    speak("Thank you sir and have a good day")
                else:
                    speak("Thank you sir and good night")
                exit()
            elif "buy" in query or "ok" in query:
                hour=int(datetime.datetime.now().hour)
                if hour>=0 and hour<=16:
                    speak("Thank you sir and have a good day")
                else:
                    speak("Thank you sir and good night")
                exit()
            
