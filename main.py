import pyautogui
import webbrowser
import time 
webbrowser.open("web.whatsapp.com")
time.sleep(30)
count=1
while count < 5:
    pyautogui.press("R")
    pyautogui.press("enter")
    count=count+1
