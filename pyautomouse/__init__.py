import pyautogui
import time

pyautogui.FAILSAFE = False


class Mouse(object):
    def __init__(self):
        super()
        self.x = 0
        self.y = 0

    def mouseClick(self,
                   count, Time=1, isdoubleclick=True, x=None, y=None, button='left', istripleClick=False):
        c = 0
        while c < count:
            if isdoubleclick:
                pyautogui.doubleClick(x=x, y=y, button=button)
            elif isdoubleclick == False:
                pyautogui.click(x=x, y=y, button=button)
            else:
                pyautogui.tripleClick(x, y, button=button)
            c += 1
            print(c)
            time.sleep(Time)

    def getMouseXY(self):
        self.x, self.y = pyautogui.position()
        return self.x, self.y

    def MoveTo(self, x, y, duration=0.25):
        pyautogui.moveTo(x=x, y=y, duration=duration)

    def dragTo(self, x, y, button='left', duration=1):
        pyautogui.dragTo(x, y, duration=duration, button=button)


class keyboard(object):
    def __init__(self):
        super()

    def hotkey(*args, count, Time=1):
        c = 0
        while c < count:
            pyautogui.hotkey(args)
            c += 1
            time.sleep(Time)

    def press(key, count, Time=1):
        c = 0
        while c < count:
            pyautogui.press(key)
            c += 1
            time.sleep(Time)

    def keyUp(key, count, Time=1):
        c = 0
        while c < count:
            pyautogui.keyUp(key)
            c += 1
            time.sleep(Time)

    def keyDown(key, count, Time=1):
        c = 0
        while c < count:
            pyautogui.keyDown(key)
            c += 1
            time.sleep(Time)

    def typewrite(key, count, Time=1):
        c = 0
        while c < count:
            pyautogui.typewrite(key)
            c += 1
            time.sleep(Time)
