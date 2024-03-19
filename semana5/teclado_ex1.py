import pyautogui

#clica no campo usuário
pyautogui.click(500, 320, duration=0.2)
#digita o numero de matricula
pyautogui.write('2022190035')

#clica no campo senha
pyautogui.click(700, 400, duration=0.2)
#digita a senha
pyautogui.write('11111111')

pyautogui.click(680, 460)