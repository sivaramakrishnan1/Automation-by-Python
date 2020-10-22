"""
THIS PROGRAM IS TO OPEN MASALA SITE IN WEB AUTOMATICALLY WHEN YOU ARE IN A RUSH... ;-)
www - 1 sec
xv - 3 
vi - 3 
llage - 1
lol - 1
"""
site="www.xvillage.lol"
switch=False
import pyautogui as p , time as t 

p.press("win")
p.write("edge")
t.sleep(1)
p.press('enter')
t.sleep(5)
p.hotkey('ctrl' , 'shift' , 'n')
t.sleep(1)
for i in range(3):
    p.write('w')
    t.sleep(0.5)
p.write(".")
t.sleep(2)
p.write('x')
t.sleep(2)
p.write('v')
t.sleep(3)
p.write('i')
t.sleep(3)
p.write('llage.')
t.sleep(2)
p.write('LoL')
