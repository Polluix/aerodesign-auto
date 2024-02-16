import pygetwindow as gw

propselector = gw.getWindowsWithTitle(' Aerodesign Propeller Selector')[0]
width, height = propselector.size
topleft_x, topleft_y = propselector.topleft
bottomright_x, bottomright_y = propselector.bottomright
allow_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'E', '.', '+', '-', '_']
screenshot_path = './result/result.png'