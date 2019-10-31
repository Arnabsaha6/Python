#Import the library needed
import pyautogui as p
import webbrowser as w
import time
#Taking input from user
x = input("Type whatever you want to search: ")
link = 'https://www.google.com/search?q={}'.format(x) 
w.open(link) 
#Delay for stability
time.sleep(1)
#Delay to let the page load
time.sleep(5)
#Moves the cursor to the search bar
p.moveTo(550,420,0.3)
#Presses enter
p.press('enter')
#Types the input provided
p.typewrite(x,0.1)
#Delay for stability
time.sleep(1)
#Presses enter
p.press('enter')