import cv2
try:
    from keras.models import load_model
except ImportError:
    load_model = None
import numpy as np
from gtts import gTTS

code={'س':0,'و':1,'ظ':2,'ط':3,'غ':4,'ف':5,'ا':6,'٣':7,'ض':8,'ث':9,'ذ':10,'٩':11,'ق':12,'١':13,'ش':14,'٤':15,'ص':16,'ب':17,'٥':18,'ت':19,'لا':20,'٠':21,'ي':22,'ج':23,'ح':24,'خ':25,'٧':26,'ز':27,'٨':28,'ه':29,'د':30,'٢':31,'ك':32,'م':33,'ر':34,'ل':35,'ن':36,'٦':37,'ع':38 }

def getname(n):
    for k,v in code.items():
        if v==n:
            return k

        

def pred_one_img(model_n,path):
    if model_n is None:
        return "Error: Model not loaded or Tensorflow missing."
    img_1=cv2.imread(path,0)
    img_1=cv2.resize(img_1,(32,32))
    img_1=np.array(img_1)
    img_1_3d=img_1.reshape((1, 32, 32))
    img_1_prob=model_n.predict(np.array(img_1_3d))
    img_1_pred=img_1_prob.argmax(axis=1)
    name_1=getname(img_1_pred)
    return f" هذا حرف ال {name_1}"

def text_to_speech(arabic_text):
    tts = gTTS(arabic_text, lang='ar')
    tts.save('test.mp3')