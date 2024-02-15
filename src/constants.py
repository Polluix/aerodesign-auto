import pygetwindow as gw

propselector = gw.getWindowsWithTitle(' Aerodesign Propeller Selector')[0]
width, height = propselector.size
topleft_x, topleft_y = propselector.topleft