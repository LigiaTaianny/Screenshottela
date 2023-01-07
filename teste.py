import pyautogui
pyautogui.screenshot()
var = pyautogui.screenshot()
var.save('Exemplo.png')
pyautogui.screenshot(region=(500, 200))
# -------------------------------------------------------------
pyautogui.mainloop()