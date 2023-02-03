from gtts import gTTS

# The text that you want to convert to speech
text = input("Enter what you want hear: ")

# Creating an instance of gTTS
tts = gTTS(text=text, lang='en', tld='com.au')

# Saving the speech to a file
tts.save("hello.mp3")
