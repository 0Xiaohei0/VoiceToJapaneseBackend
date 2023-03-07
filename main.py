import os
from fastapi import FastAPI
import azure.cognitiveservices.speech as speechsdk

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/get_speech_config")
def read_item():
    return speechsdk.SpeechConfig(subscription=os.environ.get(
        'SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
