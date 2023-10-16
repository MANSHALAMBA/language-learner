
from flask import Flask, request
from flask_cors import CORS
import openai


app = Flask(__name__)
cors = CORS(app)
openai.api_key = "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"


@app.post('/translate')
def translate():
    files = request.files
    file = files.get('file')
    file.save(open('/tmp/recording.mp3', "wb"))
    audio_file = open('/tmp/recording.mp3', "rb")
    transcript = openai.Audio.translate("whisper-1", audio_file)
    print(transcript)
    return {'translated_text': transcript['text']}

