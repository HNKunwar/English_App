import whisper

model = whisper.load_model('base')

#load audio, fit into 30 sec
audio = whisper.load_audio("output.wav")
audio = whisper.pad_or_trim(audio)

#make log Mel spectogram and move to the same device as model
mel = whisper.log_mel_spectrogram(audio).to(model.device)

#detect spoken language
_, probs = model.detect_language(mel)
#if {max(probs, key=probs.get)} == "en":

  #nxt 2 lines are depracated, bring back to simplify
   #model.transcribe('insert.wav', fp16=False)
    #output = result['text']


    #decode audio
options = whisper.DecodingOptions(fp16=False)
result = whisper.decode(model, mel, options)
print(result.text)


#else:
  #  output = "Please give a response in English!"
