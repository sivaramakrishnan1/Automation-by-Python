import pyautogui as p, time as t

p.press('win')
t.sleep(0.5)
p.write('whatsapp')
p.press('enter') 

t.sleep(10)
p.press('tab')
p.write('vish')
t.sleep(1)
p.press('enter')

t.sleep(5)
msg=["1", "2", "3", "4", "kiruba kiruba kirubaaaa", "kiruba kiruba kirubaaaaaaa"]

for i in msg:
    p.write(i)
    p.press('enter')
    t.sleep(1)