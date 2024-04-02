import pyautogui

#Mover o mouse
pyautogui.moveTo(960,540, duration=.5)
pyautogui.moveRel(100, 100, duration=.5)

#Arrastar o mouse
pyautogui.dragTo(960, 540, duration=.5)
pyautogui.dragRel(100, 100, duration=.5)

#Clicar o mouse
pyautogui.click(960, 540, duration=.5, clicks=2, button='LEFT')

#Rolagem
pyautogui.scroll(-2)

#Teclado

#Escrever
pyautogui.write('Ola', interval=0.3)

#Precionar uma tecla especifica
pyautogui.press('enter')

#Precionar teclas simultâneas
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('ctrl', 'v')

#Manter teclas pressionadas e soltar depois
pyautogui.keyDown('a')
pyautogui.keyUp('a')
