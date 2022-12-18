import pyttsx3

text_speech = pyttsx3.init()

#takes the input to convert to speech
answer = input("What do you want to convert?")
text_speech.say(answer)
text_speech.runAndWait()