from gtts import gTTS
import os

def deliver_response(response):
    tts = gTTS(response)
    tts.save("response.mp3")
    os.system("mpg321 response.mp3")  # Play the audio (Linux/Mac)