# Passo a Passo do Projeto

# Biblioteca (Pacote de Codigos do Python)
# Automatizar uma tarefa
# usaremos o (pyautogui) pois ele ira automatizar por exemplo o mouse, teclado, monitor

# 1. Abrir o sistema da empresa
import pandas  # ou pd = pandas abreveação
# https://dlp.hashtagtreinamentos.com/python/intensivao/login

# como instalar - ir ate o terminar e digitar pip install pyautogui
import pyautogui
import time

pyautogui.PAUSE = 0.5

# pyautogui.click -> clicar com mause
# pyautogui.write -> escrever um texto
# payautogui.press -> pressionar uma tecla do teclado
# payautogui.hotkey -> apertar um conjuto de teclas ( Ctrl C, Ctrl V, Alt Tab)


# abrir o navegador de sua preferencia
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# aqui pode ser que ele demore alguns swgundos para carregar o site
time.sleep(3)

# Entrar no Site do sistema
pyautogui.click(x=1654, y=58)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

# 2.Fazer login
pyautogui.press("tab")
pyautogui.write("adamsmonteiro@hotmail.com")

time.sleep(3)

# confirma se ao clicar na tecla TAB ele ira para outro campo desejado
pyautogui.press("tab")
pyautogui.write("123456")

time.sleep(3)

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

# 3.Abrir/importar a base de dados de produtos para cadastrar
# pip install pandas numpy openpyxl

tabela = pandas.read_csv("produtos.csv")

print(tabela)

# 4.Cadastrar um produto
for linha in tabela.index:
    codigo = str(tabela.loc[linha, "codigo"])
    # clicar no campo do produto
    pyautogui.click(x=1791, y=299)
    # preencher o codigo
    pyautogui.write(codigo)
    # passar pro proximo campo
    pyautogui.press("tab")

    # marca_produto
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    # passar pro proximo campo
    pyautogui.press("tab")

    # tipo_produto
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    # passar pro proximo campo
    pyautogui.press("tab")

    # categoria_produto
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    # passar pro proximo campo
    pyautogui.press("tab")

    # preço_produto
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    # passar pro proximo campo
    pyautogui.press("tab")

    # custo_produto
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    # passar pro proximo campo
    pyautogui.press("tab")

    # obs
    obs = str(tabela.loc[linha, "obs"])
    # obs for diferente de nan
    if obs != "nan":
        pyautogui.write(obs)
    # passar pro proximo campo
    pyautogui.press("tab")

    # apertar o botão
    pyautogui.press("enter")
    pyautogui.scroll(4000)


# 5.Repetir isso tudo ate acabar a lista de produtos
# FIM
