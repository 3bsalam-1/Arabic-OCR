import pytesseract
from gtts import gTTS
import cv2


def check_tesseract_availability():
    try:
        pytesseract.get_tesseract_version()
        return True
    except pytesseract.TesseractNotFoundError:
        return False
    except FileNotFoundError:
        return False
    except Exception:
        return False

def image_to_text(filename):
    if not check_tesseract_availability():
        raise EnvironmentError("Tesseract is not installed or not found in PATH.")
        
    img_cv = cv2.imread(filename)
    if img_cv is None:
        raise FileNotFoundError(f"Could not read image file: {filename}")
        
    arabic_text=pytesseract.image_to_string(img_cv , lang='ara',config= ".")
    return arabic_text


def text_to_speech(arabic_text):
    tts = gTTS(arabic_text, lang='ar')
    tts.save('test.mp3')

