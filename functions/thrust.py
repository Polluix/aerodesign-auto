import pyautogui
from src.constants import topleft_x, topleft_y, width, height

def changeThrust():
    pyautogui.moveTo((topleft_x, topleft_y))
    pyautogui.moveTo((topleft_x + width*0.93, topleft_y + height*0.5))
    pyautogui.click()
    pos_x, pos_y = pyautogui.position()
    pyautogui.moveTo((pos_x-width*0.05, pos_y+height*0.15))
    pyautogui.click()