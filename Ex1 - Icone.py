import pyautogui

pyautogui.moveTo(260,220,duration=1)
pyautogui.doubleClick(260,220,interval=3)
pyautogui.write('Teste Python', interval=0.2)
pyautogui.press('enter')