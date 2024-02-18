def getWindow():
    
    import pyautogui

    option1 = ' AeroDesign Propeller Selector'
    option2 = 'Propeller Selector'

    windows = pyautogui.getAllWindows()

    titles=[]

    for x in windows:
        titles.append(x.title)

    index1 = titles.index(option1)
    index2 = titles.index(option2)

    return option1 if index1 < index2 else option2

