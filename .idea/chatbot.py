from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)

import pyttsx3
text_speech = pyttsx3.init()

import pyaudio
import wave

import whisper

import os

bot = ChatBot(
    name="Bot",
    read_only=True,
    logic_adapters=["chatterbot.logic.MathematicalEvaluation",
                    "chatterbot.logic.BestMatch",
                    ],
    preprocessors=['chatterbot.preprocessors.clean_whitespace',
                   'chatterbot.preprocessors.unescape_html',
                   'chatterbot.preprocessors.convert_to_ascii']
)


# run and get response from user.

text_speech.say('What should I call you?')
text_speech.runAndWait()
name = input('What should I call you?')


print ('Hi ' + name + '! How are you today?')
text_speech.say('Hi ' + name + '! How are you today?')
text_speech.runAndWait()
while True:
    #captures audio
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("start speaking...")

    frames = []
    seconds = 4
    for i in range(0, int(RATE / CHUNK * seconds)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Recording stopped.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open("output.wav", 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    #audio to text
    model = whisper.load_model('base')

    #load audio, fit into 30 sec
    audio = whisper.load_audio("output.wav")
    audio = whisper.pad_or_trim(audio)

    #make log Mel spectogram and move to the same device as model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    #detect spoken language
    _, probs = model.detect_language(mel)

    #decode audio
    options = whisper.DecodingOptions(fp16=False)
    result = whisper.decode(model, mel, options)



    request = name+': '+result.text
    print(request)

    if request=="Bye" or request=='bye':
        print('Bot: Bye')
        break
    else:
        response=bot.get_response(request)
        botresponse = str(response)
        text_speech.say(botresponse)
        text_speech.runAndWait()
        print('Bot: ', response)
        os.remove("output.wav")


