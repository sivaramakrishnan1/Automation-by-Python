import pyautogui,time


pyautogui.press('win')
pyautogui.write('paint')
pyautogui.press('enter')
time.sleep(2)

pyautogui.moveTo(400, 400)

distance = 200
while distance > 0:
        pyautogui.drag(distance, 0, duration=0.5)   # move right
        distance -= 20
        pyautogui.drag(0, distance, duration=0.5)   # move down
        pyautogui.drag(-distance, 0, duration=0.5)  # move left
        distance -= 20
        pyautogui.drag(0, -distance, duration=0.5)  # move up

