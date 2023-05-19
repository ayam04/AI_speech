import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
from pygame import mixer

def fridayeasteregg():
        mixer.init()
        mixer.music.load('e:/LOCAL/Betrayer/Metalik Klinik1-Anak Sekolah.mp3')
        mixer.music.play()
        
def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print('Listening')
		r.pause_threshold = 0.7
		audio = r.listen(source)
		try:
			print("Recognizing")
			Query = r.recognize_google(audio, language='en-in')
			print("the command is printed=", Query)
			
		except Exception as e:
			print(e)
			print("Say that again sir")
			return "None"
		
		return Query

def speak(audio):
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')
	engine.setProperty('voice', voices[0].id)
	engine.say(audio)
	engine.runAndWait()

def tellDay():
	day = datetime.datetime.today().weekday() + 1
	Day_dict = {1: 'Monday', 2: 'Tuesday',
				3: 'Wednesday', 4: 'Thursday',
				5: 'Friday', 6: 'Saturday',
				7: 'Sunday'}
	
	if day in Day_dict.keys():
		day_of_the_week = Day_dict[day]
		print(day_of_the_week)
		speak("The day is " + day_of_the_week)


def tellTime():
	time = str(datetime.datetime.now())
	print(time)
	hour = time[11:13]
	min = time[14:16]
	speak(self, "The time is sir" + hour + "Hours and" + min + "Minutes")

def Hello():
	print("hello sir I am your desktop assistant.Tell me how may I help you today")
	speak("hello sir I am your desktop assistant.Tell me how may I help you today")


def Take_query():
	Hello()
	while(True):
            
		query = takeCommand().lower()
		if "open instgram" in query:
			print("Opening instgram ")
			speak("Opening instgram ")
			webbrowser.open("www.instagram.com")
			break
                
		elif "open google" in query:
			print("Opening Google ")
			speak("Opening Google ")
			webbrowser.open("www.google.com")
			break
			
		elif "what is the day today" in query:
			tellDay()
			break
		
		elif "tell me the time" in query:
			tellTime()
			break
		
		elif "from wikipedia" in query:
			print("Checking the wikipedia, give me a second ")
			speak("Checking the wikipedia, give me a second ")
			query = query.replace("wikipedia", "")
			result = wikipedia.summary(query, sentences=4)
			print("According to wikipedia")
			speak("According to wikipedia")
			print(result)
			speak(result)
		
		elif "tell me your name" in query:
			print("I am Core, ayam's assistant")
			speak("I am Core, ayam's assistant")

		elif "bye" in query:
			print("Bye Sir")
			speak("Bye Sir")
			exit()	

if __name__ == '__main__':
	Take_query()
