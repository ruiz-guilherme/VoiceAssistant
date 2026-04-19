from IPython.display import Audio, display, Javascript
from google.colab import output
from base64 import b64decode

RECORD = """ ... seu JS aqui ... """

def record_audio(sec=5):
    display(Javascript(RECORD))
    js_result = output.eval_js(f'record({sec * 1000})')
    audio = b64decode(js_result.split(',')[1])

    file_name = 'audio/input/request_audio.wav'
    with open(file_name, 'wb') as f:
        f.write(audio)

    display(Audio(file_name, autoplay=False))
    return file_name
