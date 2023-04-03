import pyautogui as gs

def myFunc():
    im1 = gs.screenshot()

    im1.save('screenshot.png')

myFunc()
