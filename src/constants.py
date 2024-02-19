import pygetwindow as gw
from src.getWindow import getWindow

title = getWindow()

propselector = gw.getWindowsWithTitle(title)[0]
width, height = propselector.size
topleft_x, topleft_y = propselector.topleft
bottomright_x, bottomright_y = propselector.bottomright
allow_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'E', '.', '+', '-', '_']
