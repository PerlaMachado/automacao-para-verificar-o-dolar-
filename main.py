import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

# LEMBRANDO: O HOTKEY ESTÁ POSICIONADO DE ACORDO COM A MINHA TELA, CASO PRECISE DE AJUSTE, USE O ARQUIVO "pegar_posicao.py".

# Vamos abrir primeiro o site.

pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=387, y=77)
pyautogui.write("https://www.bcb.gov.br/estabilidadefinanceira/historicocotacoes")
pyautogui.press("enter")


# Tempo para a página carregar

pyautogui.PAUSE = 5


# Agora vamos editar os dados para pegar o que realmente queremos.

pyautogui.click(x=539, y=669)
pyautogui.doubleClick(x=539, y=669)
pyautogui.hotkey("ctrl", "a")
pyautogui.press("delete")
pyautogui.write("01012026")
pyautogui.press("tab")
pyautogui.hotkey("ctrl", "a")
pyautogui.press("delete")
pyautogui.write("31012026")
pyautogui.press("tab")
pyautogui.press("left", presses=8)
pyautogui.press("tab")
pyautogui.press("enter")

# E ele vai dar esperado, a tabela de cotação. 