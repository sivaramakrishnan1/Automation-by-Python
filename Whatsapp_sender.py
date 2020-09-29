import pyautogui, time

pyautogui.press('win')
pyautogui.write('whatsapp')
pyautogui.press('enter')

time.sleep(10)
time.sleep(3)
for i in range(2):
    pyautogui.press('tab')

pyautogui.press('down')
pyautogui.press('enter')

time.sleep(3)
pyautogui.write("This is an auto generated message, *Mua ha ha* ")
