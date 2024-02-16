from src.constants import propselector
from functions.velocity import changeVelocity, setZero
from functions.thrust import changeThrust
from src.constants import *
import pyautogui
from PIL import Image
import pytesseract as pyt
import cv2

propselector.activate()

setZero()
changeVelocity()
changeThrust()

#TODO: transform in function
screenshot_path = './result/result.png'
pyt.pytesseract.tesseract_cmd = 'D:/Program Files/Tesseract-OCR/tesseract.exe'

pyautogui.screenshot(screenshot_path)
im = Image.open(screenshot_path)
im = im.crop((topleft_x+10, topleft_y-10, bottomright_x-10, bottomright_y+10))
im.save(screenshot_path)

im = cv2.imread(screenshot_path)
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) 

text = pyt.image_to_string(gray)
print(text)


# propselector.close()