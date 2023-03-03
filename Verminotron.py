# Por: Akinori Koerich
# GitHub: https://github.com/AkinoriKoerich
# Programa elaborado para fins educacionais.



# Importando as bibliotecas
import customtkinter
import pyautogui
import time
import pyperclip



# passando parametros (customtkinter)
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

# criando a janela
janela = customtkinter.CTk()
janela.geometry('700x500')
   
def validate_num(new_value):
    return new_value.isdigit() or new_value == ""

def on_click(event):
    Qnt.delete(0, customtkinter.END)
    Qnt.unbind('<Button-1>', on_click_id)

def salvar_numeros():
    global num1, nav2, cont2, msg2
    num1 = int(Qnt.get())
    print(type(num1))
    nav2 = Nav.get()
    cont2= Cont.get()
    msg2 = Msg.get()
    
def fechar_programa():
    janela.destroy()    

def salvar_e_fechar():
    salvar_numeros()
    fechar_programa()

# Criando o texto
texto = customtkinter.CTkLabel(janela, text='Verminotron')
texto.pack(padx=10, pady=10)

# Criando entradas de texto

Nav = customtkinter.CTkEntry(janela, placeholder_text='Digite seu navegador')
Nav.pack(padx=10, pady=10)

Cont = customtkinter.CTkEntry(janela, placeholder_text='Digite o contato')
Cont.pack(padx=10, pady=10)

Msg = customtkinter.CTkEntry(janela, placeholder_text='Digite a mensagem')
Msg.pack(padx=10, pady=10)

texto2 = customtkinter.CTkLabel(janela, text='Quantidade')
texto2.pack(padx=10, pady=10)
Qnt = customtkinter.CTkEntry(janela, validate="key", validatecommand=(janela.register(validate_num), '%S'))
Qnt.pack(padx=10, pady=10)
Qnt.insert(0, "Digite um número") # Adiciona o placeholder
on_click_id = Qnt.bind('<Button-1>', on_click)

check = customtkinter.CTkCheckBox(janela, text='Continuar?')
check.pack(padx=10, pady=10)

lb = customtkinter.CTkLabel(janela, text='Verminotron 1.0')
lb.pack(padx=10, pady=10)


# Criando o botão
botao_salvar_fechar = customtkinter.CTkButton(janela, text="Salvar e Fechar", command=salvar_e_fechar)
botao_salvar_fechar.pack()

# Loop de janela
janela.mainloop()

# Pesquisar o navegador
pyautogui.press("win")
time.sleep(1.3)
pyautogui.write(nav2)
time.sleep(1.3)
pyautogui.press("enter")
time.sleep(4)

# Localizar o alvo desejado
pyautogui.write("web.whatsapp.com")
pyautogui.press("Enter")
time.sleep(5)

# Localizar o contato escolhido
for tab in range(5):
    pyautogui.press('Tab')
pyautogui.write(cont2)
time.sleep(1.3)
pyautogui.press('enter')

# Digitar a mensagem

formatado = int(num1)

for num in range(formatado):
    pyperclip.copy(msg2)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 'w')
