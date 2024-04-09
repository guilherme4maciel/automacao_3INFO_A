import pyautogui, pyscreeze

#localizar x, y de uma imagem na tela
menuEdit_XY = pyautogui.locateCenterOnScreen('./semana7/digite_nome.png', confidence=0.9)

pyautogui.click(menuEdit_XY, duration= 0.5)
pyautogui.write('Guilherme Henrique Maciel Alves', interval=0.2)

menuEdit_XY = pyautogui.locateCenterOnScreen('./semana7/digite_cpf.png', confidence=0.9)
pyautogui.click(menuEdit_XY, duration= 0.5)
pyautogui.write('02187623645', interval=0.2)

menuEdit_XY = pyautogui.locateCenterOnScreen('./semana7/sim.png', confidence=0.9)
pyautogui.click(menuEdit_XY, duration= 0.5)

menuEdit_XY = pyautogui.locateCenterOnScreen('./semana7/enviar.png', confidence=0.9)
pyautogui.click(menuEdit_XY, duration= 0.5)


