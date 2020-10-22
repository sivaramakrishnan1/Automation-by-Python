"""
This program will send a message to the most recent whatsapp message sent/ recieved chat. 
You can change the message by changing msg variable
"""
import pyautogui as p, time as t


contact=list(map(str, input("Enter a contact name: ").split()))
msg= "hi" #The message
p.press('win')
p.write('whatsapp')
p.press('enter')

#Waiting to open whatsapp
t.sleep(10)

#Navigating to the recent chat
p.press('tab')

for i in contact:
    p.write(i)
    t.sleep(3)
    p.press('enter')
    t.sleep(2)
    p.write(msg) #Typing the message 
    t.sleep(2)
    p.press('enter')
    t.sleep(2)
    p.keyDown("shift")
    p.press('tab')
    t.sleep(0.5)
    p.press('tab')
    t.sleep(0.5)
    p.press('tab')
    t.sleep(0.5)
    p.keyUp("shift")

