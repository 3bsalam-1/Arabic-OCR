import pytesseract
from gtts import gTTS
import cv2


def image_to_text(filename):
    img_cv = cv2.imread(filename)
    arabic_text=pytesseract.image_to_string(img_cv , lang='ara',config= ".")
    return arabic_text


def text_to_speech(arabic_text):
    tts = gTTS(arabic_text, lang='ar')
    tts.save('test.mp3')

