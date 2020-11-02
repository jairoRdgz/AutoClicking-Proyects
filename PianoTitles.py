import pyautogui
import time
import keyboard
import win32api
import win32con

#celda 1 = X:  520 Y:  500 RGB: (1, 1, 1)
#celda 2 = X:  630 Y:  500 RGB: (1, 1, 1)
#celda 3 = X:  740 Y:  500 RGB: (1, 1, 1)
#celda 4 = X:  840 Y:  500 RGB: (1, 1, 1)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed('q') == False :

    if pyautogui.pixel(520, 500)[0] == 0:
        click(520, 500)
    if pyautogui.pixel(630, 500)[0] == 0:
        click(630, 500)
    if pyautogui.pixel(740, 500)[0] == 0:
        click(740, 500)
    if pyautogui.pixel(840, 500)[0] == 0:
        click(840, 500)
