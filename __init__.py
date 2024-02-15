import pygetwindow as gw
import pyautogui
from src.constants import propselector, width, height, topleft_x, topleft_y
from functions.velocity import changeVelocity, setZero


propselector.activate()

setZero()
changeVelocity()


# propselector.close()