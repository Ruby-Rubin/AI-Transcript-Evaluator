import whisper

def generate_transcript(video_path):
    model = whisper.load_model("base")

    result = model.transcribe(video_path)
    print('Transcript generated successfully!')

    return result["text"]
