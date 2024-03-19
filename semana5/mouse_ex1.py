import pyautogui

'pyautogui.moveTo(700, 400, duration=0.2)'

#moveRel é relativo, então ele não vai mexer o y
pyautogui.moveRel(-400, 0, duration=0.2)
pyautogui.moveRel(0, 400, duration=0.2)
pyautogui.moveRel(400, 0, duration=0.2)
pyautogui.moveRel(0, -400, duration=0.2)