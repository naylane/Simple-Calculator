import tkinter
from tkinter import PhotoImage

# Configurações da janela principal
window = tkinter.Tk()
window.title("Calculadora")
window.geometry("402x460")
window.resizable(False, False)
window.configure(bg="#f6f6f8")
window.iconphoto(False, PhotoImage(file="./img/icon.png"))

# Variável que será usada para armazenar as equações digitadas
equation = ""

def show(value):
    global equation
    equation += value
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def backspace():
    global equation
    equation = equation[:-1]
    label_result.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
            equation = ""
        except:
            result = "Equação inválida."
            equation = ""
    label_result.config(text=result)

# Função para criar botões
def create_button(text, x, y, width=4, height=1, command=None, bg="#f49345"):
    btn = tkinter.Button(window, text=text, width=width, height=height, font=("arial", 20, "bold"), bd=1, fg="#fff", bg=bg, command=command).place(x=x, y=y)
    
    return btn

# Tela
label_result = tkinter.Label(window, width=25, height=2, text="", font=("arial", 25))
label_result.pack()

# Botões
create_button("C", 10, 100, command=lambda: clear(), bg="#e06c49")
create_button("/", 110, 100, command=lambda: show("/"))
create_button("%", 210, 100, command=lambda: show("%"))
create_button("*", 310, 100, command=lambda: show("*"))

create_button("7", 10, 170, command=lambda: show("7"))
create_button("8", 110, 170, command=lambda: show("8"))
create_button("9", 210, 170, command=lambda: show("9"))
create_button("+", 310, 170, command=lambda: show("+"))

create_button("4", 10, 240, command=lambda: show("4"))
create_button("5", 110, 240, command=lambda: show("5"))
create_button("6", 210, 240, command=lambda: show("6"))
create_button("-", 310, 240, command=lambda: show("-"))

create_button("1", 10, 310, command=lambda: show("1"))
create_button("2", 110, 310, command=lambda: show("2"))
create_button("3", 210, 310, command=lambda: show("3"))
create_button("<", 310, 310, command=lambda: backspace(), bg="#ffbe98")

create_button("0", 10, 380, width=10, command=lambda: show("0"))
create_button(".", 210, 380, command=lambda: show("."))
create_button("=", 310, 380, command=lambda: calculate(), bg="#d2e0ed")

window.mainloop()
