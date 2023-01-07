import pyautogui
from time import sleep
from tkinter import *

# -------------------------------------------------------------

# cor

branco = '#ffffff'
azul = '#364a85'
vermelho = '#b53128'
lilas = '#C8A2C8'


# -------------------------------------------------------------

# tela
tela1 = Tk()
tela1.title('Finder')
tela1.geometry('480x400+600+200')
tela1.wm_resizable(width=False, height=False)

# labels e entrys

lb_agenda = Label(tela1, text='Find Person', font='Time 20 bold', bg=lilas, fg=branco, anchor='w', padx=10)
lb_agenda.place(width=480, height=50, x=0, y=0, )

lb_nome = Label(tela1, text='Name', font='Time 12')
lb_nome.place(width=70, height=20, x=10, y=70)
input_nome = Entry(tela1, font='Time 12')
input_nome.place(width=350, height=20, x=100, y=70)

lb_tel = Label(tela1, text='Phone', font='Time 12')
lb_tel.place(width=70, height=20, x=10, y=110)
input_tel = Entry(tela1, font='Time 12')
input_tel.place(width=350, height=20, x=100, y=110)

lb_end = Label(tela1, text='Adress', font='Time 12')
lb_end.place(width=70, height=20, x=10, y=150)
input_end = Entry(tela1, font='Time 12')
input_end.place(width=350, height=20, x=100, y=150)

# -------------------------------------------------------------

# funções


def adicionar():

    nome = input_nome.get()
    tel = input_tel.get()
    end = input_end.get()

    with open('finder.txt', 'a') as arquivo:
        arquivo.write(nome + '\n' + tel + '\n' + end + '\n')

    pyautogui.alert('Cadastro Efetuado com Sucesso!')
    input_nome.delete('0', 'end')
    input_tel.delete('0', 'end')
    input_end.delete('0', 'end')


def procurar():

    global linha
    global a_tel
    global b_end

    nome = input_nome.get()

    with open('finder.txt', 'r') as arquivo:
        for linha in arquivo:
            if nome in linha:
                a_tel = (arquivo.readline())
                b_end = (arquivo.readline())

                l_nome_busca = Label(tela1, text=linha, font='Times 10', anchor='w')
                l_nome_busca.place(width=250, height=30, x=20, y=260)
                l_tel_busca = Label(tela1, text=a_tel, font='Times 10', anchor='w')
                l_tel_busca.place(width=250, height=30, x=20, y=280)
                l_end_busca = Label(tela1, text=b_end, font='Times 10', anchor='w')
                l_end_busca.place(width=250, height=30, x=20, y=300)


def web():

    # iniciar
    pyautogui.alert('Iremos iniciar as buscas ...')
    sleep(1)
    pyautogui.press('win')
    sleep(0.5)
    pyautogui.write('Opera GX')
    sleep(1)
    pyautogui.press('enter')
    # Linkedin
    sleep(4)
    pyautogui.write('http://linkedin.com/')
    sleep(1)
    pyautogui.press('enter')
    sleep(6)
    pyautogui.press(['tab', 'tab','tab','tab','tab'])
    sleep(2)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.write(linha, interval=0.05)
    pyautogui.press('enter')
    # Ligaram
    sleep(3)
    pyautogui.hotkey('ctrl', 't')
    sleep(1)
    pyautogui.write('http://ligaram-me.com/')
    sleep(1)
    pyautogui.press('enter')
    sleep(3)
    pyautogui.press(['tab', 'tab', 'tab', 'tab','tab'])
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.write(a_tel, interval=0.05)
    pyautogui.press('enter')
    # Maps
    sleep(3)
    pyautogui.hotkey('ctrl', 't')
    sleep(1)
    pyautogui.write('https://www.google.pt/maps')
    sleep(1)
    pyautogui.press('enter')
    sleep(6)
    pyautogui.write(b_end, interval=0.05)
    pyautogui.press('enter')
    sleep(3)
    pyautogui.click('direcaomapss.png')


# -------------------------------------------------------------

# botões

b_adicionar = Button(tela1, text='Add', command=adicionar, font='Time 10 bold', bg=lilas, fg=branco)
b_adicionar.place(width=100, height=30, x=130, y=190)

b_procurar = Button(tela1, text='Search', command=procurar, font='Time 10 bold', bg=lilas, fg=branco)
b_procurar.place(width=100, height=30, x=300, y=190)

b_web = Button(tela1, text='WEB', command=web, font='Time 12 bold', bg=vermelho, fg=branco)
b_web.place(width=150, height=40, x=190, y=350)

# -------------------------------------------------------------
tela1.mainloop()