import speech_recognition as sr 
import pyaudio

                                                                       
r = sr.Recognizer()                                                                                   
with sr.Microphone() as source: 
	r.adjust_for_ambient_noise(source)                                                                       
	print("speak with ur sweet vocal-cord ...")	
	audio = r.listen(source)  # get audio from the microphone
	print("Done")  

try:
	text=r.recognize_google(audio,language='hi-IN') #google api for hindi
	print("You said .." )
	print(text) #printing your sweet voice  to  text form
	
except sr.UnknownValueError:
	print("Could not understand audio")
except sr.RequestError as e:
	print("Could not request results; {0}".format(e))


'''
if your voice does not recognize
pip install --upgrade gcloud
pip install --upgrade google-api-python-client
'''
