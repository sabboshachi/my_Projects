from gtts import gTTS

filename = "testfile.txt"
with open(filename) as file_object:
    content = file_object.read()

# The text that you want to convert to speech
text = content

# Creating an instance of gTTS
tts = gTTS(text=text, lang='en', tld='co.in')

# Saving the speech to a file
tts.save("ML.mp3")
