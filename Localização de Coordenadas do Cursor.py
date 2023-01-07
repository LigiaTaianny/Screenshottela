import pyautogui

while True:
    opc=int(input('0 - Sair \n1 - Deseja as coordenadas da tela? '))
    if opc==1:
        print(pyautogui.position())
    else:
        break