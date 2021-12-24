import pyautogui as py
import time
button=None
button2=None
def automatisme():
    button=py.locateOnScreen('Capture.PNG',region=(420,480 , 733, 880),grayscale=True)
    button2=py.locateOnScreen('Capture4.PNG',region=(420,480 , 733, 880),grayscale=True)
    if button != None or button2 != None :
        py.alert("help")
        print(button)
        KeyboardInterrupt()
    else :
        py.write("%f")
        py.press('enter')
        automatisme()
