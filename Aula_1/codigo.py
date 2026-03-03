# Lógica de Programação
# Primeiro Passo: Abrir o Navegador
# Segundo Passo: Pesquisar/Entrar na página
# Terceiro Passo: Login no Sistema
# Quarto Passo: Abrir o Banco de Dados
# Quinto Passo: Cadastrar os produtos

# pyautogui.click -> Clicar ( como se fosse um mouse )
# pyautogui.write -> Escrever um texto
# pyautogui.press -> Pressiona uma tecla
# pyautogui.hotkey -> Atalhos

import pyautogui
import time
import pandas

pyautogui.PAUSE = 3

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Primeiro Passo

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(4)
pyautogui.click(x=521, y=430)
time.sleep(4)

# Segundo Passo

pyautogui.write(link)
pyautogui.press("enter")
time.sleep(5)

# Terceiro Passo

pyautogui.click(x=540, y=376)
pyautogui.write("teste@teste.com")
pyautogui.press("tab")
pyautogui.write("senha muito dificil")
pyautogui.press("tab")
pyautogui.press("enter")

# Quarto Passo 

tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:

    pyautogui.click(x=518, y=259)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.scroll(1000)


# OBS: Ativar a venv e rodar pelo terminal 