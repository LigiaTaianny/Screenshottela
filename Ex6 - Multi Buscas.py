import pyautogui
from time import sleep
from tkinter import *

#-------------------------------------------------------------

#tela
tela1 = Tk()
Img=PhotoImage(file='Buscador.png')
tela1.title('Multi Buscador')
tela1.geometry('350x460+500+100')
tela1.wm_resizable(width=False, height=False)

#imagem
l_buscador=Label(tela1,image=Img)
l_buscador.place(width=350, height=350, x=0, y=0)

#input
input_buscar=Entry(tela1, font=('Time 15 bold'))
input_buscar.place(width=250, height=40, x=50, y=360)

#-------------------------------------------------------------

#função bot

def bot():
    palavra = input_buscar.get()
    pyautogui.alert('Iremos iniciar as buscas ...')
    sleep(1)
    #Google
    pyautogui.press('win')
    pyautogui.write('Opera Gx')
    sleep(2)
    pyautogui.press('enter')
    sleep(4)
    pyautogui.write(palavra, interval=0.05)
    pyautogui.press('enter')
    #Wikipedia
    sleep(3)
    pyautogui.hotkey('ctrl', 't')
    sleep(2)
    pyautogui.write('pt.wikipedia.org')
    sleep(3)
    pyautogui.press('enter')
    sleep(3)
    pyautogui.press(['tab', 'tab', 'tab', 'tab'])
    pyautogui.write(palavra, interval=0.05)
    pyautogui.press('enter')
    # Youtube
    sleep(3)
    pyautogui.hotkey('ctrl', 't')
    sleep(2)
    pyautogui.write('https://www.youtube.com/')
    sleep(3)
    pyautogui.press('enter')
    sleep(6)
    pyautogui.press(['tab', 'tab', 'tab', 'tab'])
    pyautogui.write(palavra, interval=0.05)
    pyautogui.press('enter')
    # Dicionario
    sleep(3)
    pyautogui.hotkey('ctrl', 't')
    sleep(2)
    pyautogui.write('dicionario.priberam.org')
    sleep(3)
    pyautogui.press('enter')
    sleep(2)
    pyautogui.write(palavra, interval=0.05)
    pyautogui.press('enter')

#-------------------------------------------------------------

#botão

b_buscar=Button(tela1, text='Buscar', command=bot, font=('Stencil 15 bold'))
b_buscar.place(width=100, height=40, x=130, y=410)


#-------------------------------------------------------------
tela1.mainloop()