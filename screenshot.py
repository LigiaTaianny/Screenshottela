import pyautogui
pyautogui.screenshot()
var = pyautogui.screenshot()
var.save('exemplo.png')
pyautogui.screenshot(region= (500,100))
pyautogui.mainloop()
