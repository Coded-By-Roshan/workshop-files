from email import message
import pyttsx3 
import wikipedia
import webbrowser

speech = pyttsx3.init()
voice = speech.getProperty('voices')
rate = speech.getProperty('rate')
speech.setProperty('voice',voice[1].id)
speech.setProperty('rate',200)
# message = "this is the workshop this is the workshop this is the workshop"
message = input("Enter message to speak: ")
# info = wikipedia.summary(message, sentences=2)..............................
# speech.say("According to wikipedia ")
# speech.say(info)
# speech.runAndWait()
