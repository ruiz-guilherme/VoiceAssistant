import whisper

model = whisper.load_model("small")

def transcribe_audio(audio_path, language="pt"):
    result = model.transcribe(audio_path, fp16=False, language=language)
    return result["text"]
