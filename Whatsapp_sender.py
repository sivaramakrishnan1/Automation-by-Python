"""
This program will send a message to the most recent whatsapp message sent/ recieved chat. 
You can change the message by changing msg variable
"""
import pyautogui as p, time as t

msg= "Your message goes here" #The message
open_time = 30  #The time that whatsapp might take to open in slower systems

#opening whatsapp
p.press('win')
p.write('whatsapp')
p.press('enter')

#Waiting to open whatsapp
t.sleep(open_time)
t.sleep(3)

#Navigating to the recent chat
p.press('tab')
p.press('down')
p.press('enter')
p.write(msg) #Typing the message 
p.press('enter')


