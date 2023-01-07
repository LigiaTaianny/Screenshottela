import pyautogui
from time import sleep

pyautogui.press('win')
sleep(1)
pyautogui.write('paint')
sleep(1)
pyautogui.press('enter')
sleep(2)
pyautogui.click(x=350, y=90)
pyautogui.click (x=310, y=250)
sleep(3)
pyautogui.mouseDown()
sleep(1)
pyautogui.dragTo(310,450, duration=0.5)
pyautogui.dragTo (510,450, duration=0.5)
pyautogui.dragTo(510,250, duration=0.5)
pyautogui.dragTo(310,250, duration=0.5)
pyautogui.mouseUp()