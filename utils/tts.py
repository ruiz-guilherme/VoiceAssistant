from gtts import gTTS
from IPython.display import Audio, display

def generate_audio(text, language="pt"):
    output_path = 'audio/output/response.wav'

    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(output_path)

    display(Audio(output_path, autoplay=True))
    return output_path
