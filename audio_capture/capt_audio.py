import ffmpeg

def capt_audio(output_file="audio_chunk.mp3"):
    # Use ffmpeg to capture system audio (adjust based on your OS)
    (
        ffmpeg.input(":0")  # Capture system audio (Linux/Mac)
        .output(output_file, format="mp3", ar=16000)
        .run()
    )
    return output_file