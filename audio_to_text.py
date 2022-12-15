import speech_recognition as sr


recon = sr.Recognizer()

PATH = 'wind.wav'

with sr.AudioFile(PATH) as source:
    audio = recon.record(source)

text = recon.recognize_sphinx(audio)


print(text)

