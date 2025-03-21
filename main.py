from audio_capture.capture_audio import capture_audio
from speech_to_text.transcribe import transcribe_audio
from question_detection.detect_questions import detect_question
from ai_answering.answer_questions import answer_question
from response_delivery.deliver_response import deliver_response

def main():
    # Step 1: Capture audio
    audio_file = capt_audio()

    # Step 2: Transcribe audio
    transcript = transcribe_audio(audio_file)

    # Step 3: Detect questions
    if detect_question(transcript):
        # Step 4: Generate answer
        answer = answer_question(transcript)

        # Step 5: Deliver response
        deliver_response(answer)

if __name__ == "__main__":
    main()