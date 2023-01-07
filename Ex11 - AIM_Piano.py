# testado no site http://poki.pt/g/piano-tiles-2
# ajuste para tela cheia e configure onde esta posicionado cada tecla do piano com o Mouse Position

import pyautogui

# (configurar conforme ajuste da tela)
# Tecla 1 - 460 400
# Tecla 2 - 525 400
# Tecla 3 - 600 400
# Tecla 4 - 660 400


pyautogui.alert('Ok para iniciar')

while True:
    if pyautogui.pixel(460, 400)[0] == 1:
        pyautogui.click(460, 400)
    if pyautogui.pixel(525, 400)[0] == 1:
        pyautogui.click(525, 400)
    if pyautogui.pixel(600, 400)[0] == 1:
        pyautogui.click(600, 400)
    if pyautogui.pixel(660, 400)[0] == 1:
        pyautogui.click(660, 400)