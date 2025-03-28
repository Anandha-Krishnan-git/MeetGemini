from google.cloud import speech_v1p1beta1 as speech

def transcribe_audio(audio_file):
    client = speech.SpeechClient()
    with open(audio_file, "rb") as f:
        audio = speech.RecognitionAudio(content=f.read())
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.MP3,
        sample_rate_hertz=16000,
        language_code="en-US",
    )
    response = client.recognize(config=config, audio=audio)
    transcript = ""
    for result in response.results:
        transcript += result.alternatives[0].transcript
    return transcript