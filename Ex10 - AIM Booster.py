import pyautogui
from time import sleep

pyautogui.alert('Ok para iniciar')

while True:

    sc = pyautogui.screenshot(region=(370,255,610,427))
    width,height = sc.size

    for x in range (0,width,5):
        for y in range (0,height,5):
            r,g,b = sc.getpixel((x,y))
            print(r,g,b)

            if r == 255 and g == 219 and b == 195:
                pyautogui.click (370+x, 255+y)
                sleep(0.2)
                break