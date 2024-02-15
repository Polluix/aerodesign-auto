import pyautogui
from src.constants import topleft_x, topleft_y, width, height

def changeVelocity():
    pyautogui.moveTo((topleft_x, topleft_y))
    pyautogui.moveTo((topleft_x + width*0.93, topleft_y + height*0.15))
    pyautogui.click()
    pos_x, pos_y = pyautogui.position()
    pyautogui.moveTo((pos_x-width*0.05, pos_y+height*0.15))
    pyautogui.click()

def setZero():
    pyautogui.moveTo((topleft_x, topleft_y))
    pyautogui.moveTo((topleft_x+0.63*width, topleft_y+0.16*height))
    pyautogui.click()
    pos_x, pos_y = pyautogui.position()
    pyautogui.moveTo((pos_x+0.05*width, pos_y-0.006*height))
    pyautogui.click()
    pos_x, pos_y = pyautogui.position()
    pyautogui.moveTo((pos_x-0.13*width, pos_y+0.006*height))
    pyautogui.click()
    pos_x, pos_y = pyautogui.position()
    pyautogui.moveTo((pos_x+0.13*width, pos_y+0.01*height))
    
    for i in range(3):
        pyautogui.click()

    
    pos_x, pos_y = pyautogui.position()
    pyautogui.moveTo((pos_x-0.11*width, pos_y-0.01*height))
    pyautogui.click()
    pyautogui.moveTo((pos_x+0.005*width, pos_y+0.01*height))

    for i in range(5):
        pyautogui.click()
