import pytesseract
from gtts import gTTS
from requests import get  # to make GET request
import cv2
from playsound import playsound
from keras.models import load_model
from tensorflow import keras
import numpy as np

def image_to_text(filename):
    img_cv = cv2.imread(filename)
    arabic_text=pytesseract.image_to_string(img_cv , lang='ara',config= ".")
    return arabic_text


def text_to_speech(arabic_text):
    tts = gTTS(arabic_text, lang='ar')
    tts.save('test.mp3')

    #ipd.Audio(audio_path, autoplay=True)
