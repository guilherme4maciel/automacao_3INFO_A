'''Fazer uma pesquisa no google, Clique no campo de pesquisa, 
após digite o texto 'como automatizar o whatsapp' após pressione a tecla enter'''

import pyautogui

pyautogui.click(460,420, duration=.5)
pyautogui.write('como automatizar o whatsapp')
pyautogui.press('enter')

pyautogui.moveTo(30, 335, duration=.5)
pyautogui.dragTo(400, 480, duration=.5)
pyautogui.hotkey('ctrl', 'c')

pyautogui.click(1050, 500, duration=.5)
pyautogui.hotkey('ctrl', 'v')

