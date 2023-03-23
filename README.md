# Conversational AI Program for Non-Native English Speakers

This is a rudimentary mock-up/proof of concept version of a program meant to conversate with non-native English speakers and provide corrections on their grammar and help them change their accent if they desired. The ultimate goal is to make it real-time, have the chatbot working, and speak to the user and listen to user input, and track errors over time to help the user fix their weak spots. The focus is mostly on grammar and syntax and, if they so choose, pronunciation.

## Structure and Dependencies Used

The program is structured as follows:

- **chatbot.py:** Initiates the conversation along with some directing. Uses the following dependencies:
    - ChatterBot: A Python library that makes it easy to generate automated responses to a user's input.
    - pyttsx3: A Python library for converting text to speech.
- **r_audio.py:** Records user input. Uses the following dependencies:
    - pyaudio: A Python library for working with audio.
    - wave: A Python library for working with .wav files.
- **speech2txt.py:** Converts the .wav file from r_audio.py to text. Uses the following dependency:
    - whisper: A Python library for speech recognition.
- **grammar.py:** Runs grammar correction on the user's text. Uses the following dependency:
    - Ginger API: A grammar and spelling correction API.

## Current Functionality

Currently, the program can:

- Talk with the chatbot in real-time.
- Use rudimentary responses from the chatbot.
- Has a 3-second response window.

## Thoughts on Improvements Needed

The following improvements are needed:

- Transition to using directed OpenAI API calls for the chat or learn to build a simple conversational AI that is enough for the purposes needed here.
- Find a workaround for dependencies that don't work well on IOS or Android, as the best use case for this would be on a mobile device.
- Improve grammar correction, as the Ginger API is not effective enough. Combining this with the rudimentary responses from the chatbot could have a net negative impact on the user. Directed and parsed OpenAI API calls might be the best solution here.
- There is an urge to make something from the ground-up for the sake of learning, even if it would be too much effort for a much worse end product.
