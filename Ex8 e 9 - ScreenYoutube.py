import pyautogui
from tkinter import *
from time import sleep

# -------------------------------------------------------------

# cor

branco = '#ffffff'
azul = '#364a85'
vermelho = '#b53128'


# -------------------------------------------------------------

# tela
tela1 = Tk()
tela1.title('Mult Shots')
tela1.geometry('350x250+500+200')
tela1.wm_resizable(width=False, height=False)

# labels e entrys

lb_titulo = Label(tela1, text='Screenshot Videos', font='Time 16 bold', bg=azul, fg=branco, anchor='w', padx=10)
lb_titulo.place(width=350, height=40, x=0, y=0, )

lb_titulo2 = Label(tela1, text='Auto Screenshot Videos', font='Time 16 bold', bg=azul, fg=branco, anchor='w', padx=10)
lb_titulo2.place(width=350, height=40, x=0, y=130, )

lb_screen = Label(tela1, text='Screen Resolution', font='Time 10', anchor='w')
lb_screen.place(width=120, height=20, x=10, y=70)
input_scx = Entry(tela1, font='Time 10')
input_scx.place(width=40, height=20, x=140, y=70)
input_scy = Entry(tela1, font='Time 10')
input_scy.place(width=40, height=20, x=190, y=70)

lb_times = Label(tela1, text='Repeat', font='Time 10', anchor='w')
lb_times.place(width=120, height=20, x=10, y=190)
input_times = Entry(tela1, font='Time 10')
input_times.place(width=30, height=20, x=70, y=190)

lb_sec = Label(tela1, text='Every sec', font='Time 10', anchor='w')
lb_sec.place(width=120, height=20, x=120, y=190)
input_sec = Entry(tela1, font='Time 10')
input_sec.place(width=30, height=20, x=200, y=190)

# -------------------------------------------------------------

# funções

cont = 0

def capture():

    global cont

    scrx = input_scx.get()
    scry = input_scy.get()
    cont += 1
    sc = pyautogui.screenshot(region=(0, 0, scrx, scry))
    sc.save('Video{}.png'.format(cont))


def start():

    global cont

    scrx = input_scx.get()
    scry = input_scy.get()
    time = input_times.get()
    sec = input_sec.get()

    pyautogui.alert('Press OK and Wait')

    for x in range(int(time)):
        cont += 1
        sc = pyautogui.screenshot(region=(0, 0, scrx, scry))
        sc.save('Video{}.png'.format(cont))
        sleep(int(sec))
    pyautogui.alert('Process Finished')

# -------------------------------------------------------------

# botões

b_capture = Button(tela1, text='Capture', command=capture, font='Time 10 bold', bg=azul, fg=branco)
b_capture.place(width=70, height=20, x=250, y=70)

b_start = Button(tela1, text='Start', command=start, font='Time 10 bold', bg=vermelho, fg=branco)
b_start.place(width=70, height=20, x=250, y=190)

# -------------------------------------------------------------
tela1.mainloop()