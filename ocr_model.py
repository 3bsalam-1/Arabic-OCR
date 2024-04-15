import matplotlib.pyplot as plt
import pytesseract
from gtts import gTTS
import IPython.display as ipd
from requests import get  # to make GET request
import cv2
from playsound import playsound

def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = get(url)
        # write to file
        file.write(response.content)

#download("https://github.com/tesseract-ocr/tessdata/raw/main/ara.traineddata","ara.traineddata")


def image_to_text(filename):
    img_cv = cv2.imread(filename)
    arabic_text=pytesseract.image_to_string(img_cv , lang='ara',config= ".")
    return arabic_text


def text_to_speech(arabic_text):
    tts = gTTS(arabic_text, lang='ar')
    tts.save('test.mp3')

    #ipd.Audio(audio_path, autoplay=True)
