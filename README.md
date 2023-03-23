# English_App

Rudimentary mock-up/proof of concept version of a program meant to conversate with non-native English speakers and provide corrections on their grammar and help them change their accent if they desired. Ultimately the goal was to make it real time, have the chat bot working, and speak to the user and listen to user input, and track errors over time to help the user fix their weak spots. Goal was to focus mostly on grammar and syntax and if they so chose pronunciation. 

Structure and Dependencies Used:

1.To initiate the conversation along w some directing in the (chatbot.py) file.
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
  
2.To turn chatbot output text into speech (txt2speech.py).
import pyttsx3

3.To record user input (r_audio.py): 
import pyaudio
import wave

3. To turn .wav file from r_audio.py to text. (speech2txt.py)
import whisper

4. To run grammar correction on the User Text (grammar.py)
Ginger API

Then these components are looped together. Best practices would have called for using the different files in an orchestrated manner, but I just shoved all of the code and imports into chatbot.py. Right now only this much works: 
-Can now talk with chatbot real time. 
-Bot (incredibly) rudimentary, 
-3 second response window.

Thoughts on Improvements Needed:
  -Transition to either using directed OpenAI API calls for the chat or learn to build a simple conversational AI enough for the purposes needed here.
  -Lot of these dependencies don't work very well on IOS or Android, haven't found a workaround yet other than remote server calls, which the best use case for this would be on a mobile device so it doesn't make sense to keep using these.
  -Grammar correction through Ginger API is horrendous. Think combined with the nut job responses the rudimentary ChatBot gives, it'd actually have a net negative impact on the user. Again, OpenAI API calls directed and parsed properly might be the best here since it does exceptionally well in that department. There is an urge to make something from the ground-up for the sake of learning even if it'd be way too much effort for a much worse end product. 
