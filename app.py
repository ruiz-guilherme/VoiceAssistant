from utils.recorder import record_audio
from utils.transcriber import transcribe_audio
from utils.chat import get_chat_response
from utils.tts import generate_audio

language = "pt"

print("Ouvindo...\n")

audio_path = record_audio()
transcription = transcribe_audio(audio_path, language)

print("Você disse:", transcription)

response = get_chat_response(transcription)

print("Resposta:", response)

output_audio = generate_audio(response, language)
