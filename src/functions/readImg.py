from src.constants import *
import pyautogui
from PIL import Image
import cv2
import numpy as np
import easyocr
import os


def readImg():
    pyautogui.screenshot(screenshot_path)
    img = Image.open(screenshot_path)
    img = img.crop((topleft_x+width*0.44, topleft_y+height*0.13, topleft_x+width*0.655, topleft_y+height*0.975))   

    current = os.getcwd()

    img_name = f'{current}/image.png'

    img.save(img_name)
    img = cv2.imread(img_name)

    lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l_channel, a, b = cv2.split(lab)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cl = clahe.apply(l_channel)

    limg = cv2.merge((cl,a,b))

    enhanced_img = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

    result = np.hstack((img, enhanced_img))

    result = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

    reader = easyocr.Reader(['en'])
    resultado = reader.readtext(result, detail=True, allowlist=allow_list)

    return resultado