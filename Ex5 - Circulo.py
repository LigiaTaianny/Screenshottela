import pyautogui
from time import sleep

pyautogui.press('win')
sleep(1)
pyautogui.write('paint')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(x=565, y=79)
pyautogui.click (x=310, y=250)
sleep(1)
pyautogui.drag(xOffset=200,yOffset=200, duration=1)