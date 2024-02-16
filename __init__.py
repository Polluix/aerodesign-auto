from src.constants import propselector
from functions.velocity import changeVelocity, setZero
from functions.thrust import changeThrust
from src.constants import *
import pyautogui
from PIL import Image

propselector.activate()

setZero()
changeVelocity()
changeThrust()

#TODO: transform in function
screenshot_path = './result/result.png'

pyautogui.screenshot(screenshot_path)
im = Image.open(screenshot_path)
im = im.crop((topleft_x+10, topleft_y-10, bottomright_x-10, bottomright_y+10))
im.save(screenshot_path)


# propselector.close()