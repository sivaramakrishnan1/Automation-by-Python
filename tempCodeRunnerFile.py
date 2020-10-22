
import pyautogui as p, time as t


contact=list(map(str, input("Enter a contact name: ").split()))
msg= "hi" #The message
p.press('win')
p.write('whatsapp')
p.press('enter')
