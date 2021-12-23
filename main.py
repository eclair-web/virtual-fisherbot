import pyautogui as py
button=0
def automatisme():
    button=py.locateOnScreen('Capture.PNG',region=(309,373 , 1150, 950))
    button2=py.locateOnScreen('Capture4.PNG',region=(309,373 , 1150, 950))
    if button != None or button2 != None :
        py.alert("help")
        print(button)
        KeyboardInterrupt()
    else :
        py.write("%f")
        py.press('enter')
        automatisme()